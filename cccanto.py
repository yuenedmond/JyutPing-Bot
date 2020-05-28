# -*- coding: utf-8 -*-

"""
info:
module for jyutpingbot.py
used to parse cccanto corpus
modified / customized from cedict.py
"""

#imports
import datetime
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/corpus/cccanto.txt'
with open(path, encoding="utf-8") as file:
    text = file.read()
    lines = text.split('\n')
    dict_lines = list(lines)
    
    def parse_line(line):
        parsed = {}
        if line == '':
            dict_lines.remove(line)
            return 0
        line = line.rstrip('/')
        line = line.split('/')
        if len(line) <= 1:
            return 0
        english = line[1]
        char_and_pinyin = line[0].split('[')
        characters = char_and_pinyin[0]
        characters = characters.split()
        traditional = characters[0]
        simplified = characters[1]
        pinyin = (line[0].split('['))[1].split(']')[0]
        pinyin = pinyin.replace("v","ü")
        jyutping = (line[0].split('{'))[1].split('}')[0]
        parsed['traditional'] = traditional
        parsed['simplified'] = simplified
        parsed['pinyin'] = pinyin
        parsed['jyutping'] = jyutping
        parsed['english'] = english
        list_of_dicts.append(parsed)
    
    def main():
        for line in dict_lines:
                parse_line(line)
        for x in range(len(list_of_dicts)-1, -1, -1):
            if "surname " in list_of_dicts[x]['english']:
                if list_of_dicts[x]['traditional'] == list_of_dicts[x+1]['traditional']:
                    list_of_dicts.pop(x)
        return list_of_dicts

list_of_dicts = []
parsed_dict = main()
dt = datetime.datetime.now()
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : cccanto corpus initialized...")