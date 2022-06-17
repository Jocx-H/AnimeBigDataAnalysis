#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import codecs
import os

if __name__ == '__main__':
    with open("../BliBli/bilibili.json", encoding="utf-8") as file:
        file_json = json.load(file)
    json_file = codecs.open('anime.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    count = 0
    for line in file_json:
        json_data = json.dumps(line, ensure_ascii=False)
        json_file.write('\t' + json_data + ',\n')
    json_file.seek(-2, os.SEEK_END)
    json_file.truncate()
    json_file.write('\n]')
    json_file.close()
