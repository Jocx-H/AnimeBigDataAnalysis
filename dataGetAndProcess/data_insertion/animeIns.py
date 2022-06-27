#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: animeIns.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 24, 2022
# ---
# !/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: animeInsert.py
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

conn = pymysql.connect(**dbconfig)
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)


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
        title = escape_string(title)
        index_show = value[j + 1]
        is_finished = value[j + 2]
        is_finished = int(is_finished)
        video_link = value[j + 3]
        cover = value[j + 4]
        pub_real_time = value[j + 5]
        pub_real_time = int(pub_real_time)
        renewal_time = value[j + 6]
        if renewal_time is None:
            renewal_time = pub_real_time
        else:
            renewal_time = int(renewal_time)
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
        introduce = escape_string(introduce)

        # sql = "INSERT INTO " \
        #       "anime(nid,url,cover,title,author) " \
        #       "VALUES (%d,'%s','%s','%s','%s')" %(nid, url, cover, title, author)
        op1 = (aid, title, index_show, is_finished, video_link, cover, pub_real_time
               , renewal_time, favorites, coins, views, danmakus, depth, media_tags, score, cm_count, introduce)
        sql = """INSERT INTO 
        anime(aid,title,index_show,is_finished,video_link,cover,pub_real_time,renewal_time,favorites,coins,views,danmakus,depth,media_tags,score,cm_count,introduce) 
        VALUES (%d,'%s','%s',%d,'%s','%s','%s',%s,%d,%d,%d,%d,%d,'%s',%f,'%s','%s')""" % op1

        cursor.execute(sql)
        conn.commit()
        # # op2 = (nid, url, cover, title, author)
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # print("success")
        #     # 提交到数据库执行
        #     conn.commit()
        # except:
        #     # 如果发生错误则回滚
        #     print("failed")
        #     conn.rollback()


if __name__ == '__main__':
    anime_json_path = '../data/anime.json'
    ins_anime(anime_json_path)
    cursor.close()
    conn.close()
