#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: animeInsTest.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 24, 2022
# ---
import pymysql
import prettytable as pt
import json
import time

# 填写数据库有关信息
dbconfig = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'xxxxxxx',
    'database': 'anime',
    'charset': 'utf8'
}

conn = pymysql.connect(**dbconfig)
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)


def trans_time(stamp: int):
    time_local = time.localtime(stamp)
    dtime = time.strftime("%Y-%m-%d", time_local)
    return dtime


def ins_anime(anime_json_path):
    # SQL 插入语句
    with open(anime_json_path, encoding="utf-8") as file:
        file_json = json.load(file)
    # 获取属性名无需重复获取
    attr = list(file_json[0].keys())
    for line in file_json:
        # attr = list(line.keys())
        value = list(line.values())
        # print(attr)
        # print(value)
        # 拼接sql方言
        aid = value[-1]
        aid = int(aid)
        j = 2
        title = value[j]
        index_show = value[j + 1]
        is_finished = value[j + 2]
        is_finished = int(is_finished)
        video_link = value[j + 3]
        cover = value[j + 4]
        pub_real_time = value[j + 5]

        # timestamp转换 Y-M-D
        # *100000数据格式不对
        pub_real_time = int(pub_real_time)
        time_local = time.localtime(pub_real_time)
        dtime = time.strftime("%Y-%m-%d", time_local)
        pub_real_time = dtime
        renewal_time = value[j + 6]
        renewal_time = int(renewal_time)
        time_local = time.localtime(renewal_time)
        dtime = time.strftime("%Y-%m-%d", time_local)
        print(dtime)
        renewal_time = dtime

        favorites = value[j + 7]
        favorites = int(favorites)
        coins = value[j + 8]
        coins = int(coins)
        views = value[j + 9]
        views = int(views)
        danmakus = value[j + 10]
        danmakus = int(danmakus)
        depth = value[j + 11]
        depth = int(depth)
        media_tags = value[j + 15]
        temp_tag = ''
        for tags in media_tags:
            temp_tag += tags
            temp_tag += ','
        media_tags = temp_tag
        score = value[-4]
        if score == "暂无评分":
            score = float(0.0)
        else:
            score = float(score)
        cm_count = value[-3]
        introduce = value[-2]
