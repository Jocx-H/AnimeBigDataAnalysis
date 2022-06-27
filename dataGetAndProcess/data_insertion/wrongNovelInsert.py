#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: wrongNovelInsert.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 25, 2022
# ---
id = [3298,
      31589,
      32507,
      33983,
      36930,
      37107,
      38676]

import pymysql
import prettytable as pt
import json
from pymysql.converters import escape_string

# 填写数据库有关信息
dbconfig = {
    'host': '124.70.91.77',
    'port': 3306,
    'user': 'root',
    'password': '12345678',
    'database': 'AnimeBigDataAnalysis',
    'charset': 'utf8'
}
import re

conn = pymysql.connect(**dbconfig)
cursor = conn.cursor()


def ins_wrong_novel(novel_json_path):
    # SQL 插入语句
    with open(novel_json_path, encoding="utf-8") as file:
        file_json = json.load(file)
    # 获取属性名无需重复获取
    attr = list(file_json[0].keys())
    for line in file_json:
        try:
            # attr = list(line.keys())
            value = list(line.values())
            # print(attr)
            # print(value)
            # 拼接sql方言
            # print(value)
            nid = value[-1]
            nid = int(nid)
            if nid not in id:
                continue
            url = value[0]
            cover = value[1]
            title = value[2]
            author = value[3]
            score = value[4]
            score = float(score[0:-2])
            # print(score)
            type = value[5]
            depth = value[6]
            depth = int(depth)
            state = value[7]
            click_cnt = value[-4]
            if click_cnt[-1] == "万":
                click_cnt = int((float(click_cnt[0:-2])) * 10000)
            else:
                click_cnt = int(click_cnt)
            update_time = value[-3]
            introduce = "暂无简介"
            op1 = (nid, url, cover, title, author, score, type, depth, state, click_cnt, update_time, introduce)
            sql = """INSERT INTO 
            novel(nid,url,cover,title,author,score,type,depth,state,click_cnt,update_time,introduce) 
            VALUES (%d,'%s','%s','%s','%s',%f,'%s',%s,'%s',%d,'%s','%s')""" % op1
            cursor.execute(sql)
            # print("success")
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print('第{}个数据有问题'.format(nid))
            continue


if __name__ == '__main__':
    novel_json_path = '../data/novel.json'
    ins_wrong_novel(novel_json_path)
