# -*- coding: utf-8 -*-

"""
info:
this script is for jyutpingbot.
jyutpingbot is a dictionary for Chinese characters and JyutPing.
it takes either as input and outputs the other.
"""

# enable console error logging
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start script
import datetime #output purposes
dt = datetime.datetime.now()
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : starting script...")

# imports
from telethon import TelegramClient, events
import ctypes
# corpus, config
import cedict
import cccanto
import cantoreading
import config

# set title
ctypes.windll.kernel32.SetConsoleTitleW(config.window_title)

# config client with 'bot' as session file
client = TelegramClient(config.session_name, config.api_id, config.api_hash).start(bot_token=config.bot_token)

@client.on(events.NewMessage)
async def mainHandler(event):
    if '/start' in event.raw_text:
        await client.send_message(event.sender_id, "Hi!")
    elif '/help' in event.raw_text:
        await client.send_message(event.sender_id, "Help!")
    else:
        await process(event.raw_text, event.sender_id)
 
#process input               
async def process(string, senderid):
    output=""
    if all(u'\u4e00' <= c <= u'\u9fff' for c in string):
        sentjyutping=[]
        sentusedin=[]
        sentsimilar=[]
        numentries=0
        numusedin=0
        entry=[]
        usedin=[]
        similar=[]
        for i in cccanto.parsed_dict:
            if string==i["traditional"] or string==i["simplified"]:
                if i["jyutping"] not in sentjyutping:
                    for j in cccanto.parsed_dict:
                        #words containing character, max 3 characters total, max 8 instances
                        if i["traditional"] in j["traditional"] and i["jyutping"] in j["jyutping"]:
                            if (int(len(j["traditional"])<=3)):
                                if j["traditional"] not in sentusedin:
                                    if numusedin<8:
                                        usedin.append(j["traditional"])
                                        sentusedin.append(j["traditional"])
                                        numusedin=numusedin+1
                        #similar pronunciation, 1 character
                        if i["jyutping"] in j["jyutping"]:
                            if (int(len(j["traditional"])<=1)):
                                if j["traditional"] not in sentsimilar:
                                    similar.append(j["traditional"])
                                    sentsimilar.append(j["traditional"])
                    traditional= i["traditional"]
                    simplified= i["simplified"]
                    entry.append([1, i["jyutping"], i["pinyin"], similar, usedin, i['english']])
                    similar=[]
                    usedin=[]
                    numusedin=0
                    numentries=numentries+1
                    sentjyutping.append(i["jyutping"])
        english=""
        for i in cantoreading.parsed_dict:
            if string==i["traditional"] or string==i["simplified"]:
                if i["jyutping"] not in sentjyutping:
                    #get definition through cedict
                    for j in cedict.parsed_dict:
                        if i["traditional"] == j["traditional"] and i["pinyin"] == j["pinyin"]:
                            english=j["english"]
                    traditional= i["traditional"]
                    simplified= i["simplified"]
                    entry.append([0, i["jyutping"], i["pinyin"], english])
                    numentries=numentries+1
                    sentjyutping.append(i["jyutping"])
        #output
        output="Traditional Chinese: " + traditional + "\n"
        output=output+"Simplified Chinese: " + simplified + "\n"
        output=output+"Number of entries: " + str(numentries)
        temp=0
        for entry in entry:
            temp=temp+1
            if entry[0]==1:
                output=output+"\n\nEntry "+str(temp)+":"
                output=output+"\nJyutPing:\t\t"+entry[1]
                output=output+"\nPinyin:\t\t"+entry[2]
                output=output+"\nMeaning:\t\t"+entry[5]
                output=output+"\nSimilar pronunciation:"
                for similar in entry[3]:
                    output=output+" "+similar
                if (len(entry[3])==0):
                    output=output+ " N/A"
                output=output+"\nUsed in:"
                for usedin in entry[4]:
                    output=output+"\n"+usedin
                if (len(entry[4])==0):
                    output=output+ " N/A"
            else:
                output=output+"\n\nEntry "+str(temp)+":"
                output=output+"\nJyutPing:\t\t"+entry[1]
                output=output+"\nPinyin:\t\t"+entry[2]
                output=output+"\nMeaning:\t\t"
                if (entry[3]!=""):
                    output=output+entry[3]
                else:
                    output=output+"N/A"
        await client.send_message(senderid, output)
        dt = datetime.datetime.now()
        print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : user: "+str(senderid)+" , output: "+traditional)
        return None
    elif (string[-1].isdigit()):
        result = await checkjyutping(string)
        if result:
            jyutping=string
            senttraditional=[]
            numentries=0
            entry=[]
            for i in cccanto.parsed_dict:
                if string==i["jyutping"]:
                    if i["traditional"] not in senttraditional:
                        jyutping= i["jyutping"]
                        entry.append([i["traditional"], i["simplified"], i['english']])
                        numentries=numentries+1
                        senttraditional.append(i["traditional"])
            english=""
            for i in cantoreading.parsed_dict:
                if string==i["jyutping"]:
                    if i["traditional"] not in senttraditional:
                        #get definition through cedict
                        for j in cedict.parsed_dict:
                            if i["traditional"] == j["traditional"] and i["pinyin"] == j["pinyin"]:
                                english=j["english"]
                        jyutping= i["jyutping"]
                        entry.append([i["traditional"], i["simplified"], english])
                        numentries=numentries+1
                        senttraditional.append(i["traditional"])
            #output
            output="JyutPing: " + jyutping + "\n"
            output=output+"Number of entries: " + str(numentries)
            temp=0
            for entry in entry:
                temp=temp+1
                output=output+"\n\nEntry "+str(temp)+":"
                output=output+"\nTraditional:\t\t"+entry[0]
                output=output+"\nSimplified:\t\t"+entry[1]
                output=output+"\nMeaning:\t\t"+entry[2]
            await client.send_message(senderid, output)
            dt = datetime.datetime.now()
            print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : user: "+str(senderid)+" , output: "+jyutping)
        else:
            await client.send_message(senderid, "Error.\nInput is not valid JyutPing.")
        return None
    else:
        await client.send_message(senderid, "Error.\nMake sure your input is either\n- all Chinese\n- in JyutPing.")
        return None

#check validity of jyutping
async def checkjyutping(input):
    # list of all possible initial and final
    initial=['b','p','m','f','d','t','n','l','g','k','ng','h','gw','kw','w','z','c','s','j']
    final=['aa','aai','aau','aam','aan','aang','aap','aat','aak',
           'a','ai','au','am','an','ang','ap','at','ak',
           'e','ei','eu','em','eng','ep','ek',
           'i','iu','im','in','ing','ip','it','ik',
           'o','oi','ou','on','ong','ot','ok',
           'u','ui','un','ung','ut','uk',
           'eoi','eon','eot','oe','oeng','oet','oek','yu''yun','yut','m','ng']
    #check validity
    # only one digit in string
    if (sum(c.isdigit() for c in input))==1:
        # tone between 1 and 9
        if (int(input[-1])>0 and int(input[-1])<10):
            #remove tone
            input=input[:-1]
            #input equals standalone final (return true)
            if (input in final):
                return True
            else:
                #first letter is an initial
                if (input[0] in initial):
                    #remove initial
                    input=input[1:]
                    #remaining string in final (return true)
                    if (input in final):
                        return True
    # if any condition is not met (return false)
    return False
    
# start client and run until stopped
client.start()
dt = datetime.datetime.now()
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : script started...")
print("------------------------------")
client.run_until_disconnected()