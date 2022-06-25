#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: cosplayIns.py
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
    'password': 'xxxxxx',
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


def ins_cosplay(cosplay_json_path):
    # SQL 插入语句
    with open(cosplay_json_path, encoding="utf-8") as file:
        file_json = json.load(file)
    # 获取属性名无需重复获取
    attr = list(file_json[0].keys())
    for line in file_json:
        # attr = list(line.keys())
        value = list(line.values())
        cosid = value[-1]
        cosid = int(cosid)
        url = value[0]
        cover = value[1]
        title = value[2]
        op1 = (cosid, url, cover, title)
        sql = """INSERT INTO 
        cosplay(cosid, url, cover, title) 
        VALUES (%d,'%s','%s','%s')""" % op1
        op2 = (cosid, url, cover, title)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            print("failed")
            conn.rollback()


if __name__ == '__main__':
    cosplay_json_path = '../data/cos.json'
    ins_cosplay(cosplay_json_path)
    cursor.close()
    conn.close()
