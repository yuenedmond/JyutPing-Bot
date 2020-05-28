# -*- coding: utf-8 -*-

"""
info:
module for jyutpingbot.py
used to parse cedict corpus
references and modified from https://github.com/rubber-duck-dragon/rubber-duck-dragon.github.io/blob/master/cc-cedict_parser/parser.py by Franki Allegra in February 2020
"""

#imports
import datetime
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/corpus/cedict.txt'
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
        pinyin = char_and_pinyin[1]
        pinyin = pinyin.rstrip()
        pinyin = pinyin.rstrip("]")
        pinyin = pinyin.replace("v","ü")
        parsed['traditional'] = traditional
        parsed['simplified'] = simplified
        parsed['pinyin'] = pinyin
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
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : cedict corpus initialized...")