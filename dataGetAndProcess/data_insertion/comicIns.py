#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: comicIns.py
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


def ins_comic(comic_json_path):
    # SQL 插入语句
    with open(comic_json_path, encoding="utf-8") as file:
        file_json = json.load(file)
    # 获取属性名无需重复获取
    attr = list(file_json[0].keys())
    for line in file_json:
        # attr = list(line.keys())
        value = list(line.values())
        # print(attr)
        # print(value)
        # 拼接sql方言
        j = 0
        cid = value[-1]
        cid = int(cid)
        url = value[j]
        cover = value[j + 1]
        title = value[j + 2]
        last_short_title = value[j + 3]
        author = value[j + 4]
        type = value[-3]
        temp_tag = ''
        for tag in type:
            temp_tag += tag + ','
        type = temp_tag
        state = value[-2]
        op1 = (cid, url, cover, title, last_short_title, author, type, state)
        sql = """INSERT INTO 
        comic(cid, url, cover, title, last_short_title, author, type, state) 
        VALUES (%d,'%s','%s','%s','%s','%s','%s','%s')""" % op1

        cursor.execute(sql)
        conn.commit()
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # 提交到数据库执行
        #     conn.commit()
        # except:
        #     # 如果发生错误则回滚
        #     print("failed")
        #     conn.rollback()


if __name__ == '__main__':
    comic_json_path = '../data/comic.json'
    ins_comic(comic_json_path)
    cursor.close()
    conn.close()
