#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import codecs
import os

if __name__ == '__main__':
    with open("comic.json", encoding="utf-8") as file:
        file_json = json.load(file)
    json_file = codecs.open('comic.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    count = 0
    for line in file_json:
        json_data = {'url': line['url'], 'cover': line['cover'], 'title': line['title'], 'last_short_title':
                      line['last_short_title'][3:].strip(), 'author': line['author'][3:].strip(),
                     'type': line['type'][3:].strip().split('/'), 'state': line['state'][3:]}
        json_data = json.dumps(json_data, ensure_ascii=False)
        json_file.write('\t' + json_data + ',\n')
    json_file.seek(-2, os.SEEK_END)
    json_file.truncate()
    json_file.write('\n]')
    json_file.close()
