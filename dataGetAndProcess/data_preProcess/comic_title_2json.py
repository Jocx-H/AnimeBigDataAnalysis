#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/25 16:14
@Author: CloudAndMist
@Description:
'''

import json
import codecs
import os
import math

max_font_size = 65
min_font_size = 18
word_num = 50
min_fre = 0
max_fre = 0

def fontSize(x):
    return (x-min_fre)*1.0/(max_fre - min_fre) * (max_font_size - min_font_size) + min_font_size

def sigmoid(x):
    return 1.0 / (1.0 + math.e**(-x))

if __name__ == '__main__':
    with open("../data/pre_comic_title_count.json", encoding="utf-8") as file:
        in_file = json.load(file)
    output = []
    total_cnt = 0
    for i in range(word_num):
        output.append([in_file[i]['word'], in_file[i]['count']])
        total_cnt += in_file[i]['count']
    max_fre = output[0][1]
    min_fre = output[-1][1]
    print("word frequences: ", output)

    out_file = codecs.open('../data/comic_title_count.json', 'w+', encoding='UTF-8')
    out_file.write('{\n\t\"Word\":{\n')
    out_file.write('\t\t\"series\":[\n')
    for (word, count) in output:
        item_json = json.dumps({'name': word, 'textSize': fontSize(count)}, ensure_ascii=False)
        out_file.write('\t\t\t' + item_json + ',\n')
    out_file.seek(-2, os.SEEK_END)
    # 使用 truncate() 方法，将后面的数据清空
    out_file.truncate()
    out_file.write('\n\t\t]\n')
    # 重新输出'\n'，并输入']'，与 open_spider(self, spider) 时输出的 '['，构成一个完整的数组格式
    out_file.write('\t}\n}')
