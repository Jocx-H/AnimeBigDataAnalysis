#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: novelInsert.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 24, 2022
# ---
import pymysql
import prettytable as pt
import json

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


def ins_novel(novel_json_path):
    # SQL 插入语句
    with open(novel_json_path, encoding="utf-8") as file:
        file_json = json.load(file)
    # 获取属性名无需重复获取
    attr = list(file_json[0].keys())
    for line in file_json:
        # attr = list(line.keys())
        value = list(line.values())
        # print(attr)
        # print(value)
        #     拼接sql方言
        print(value)
        nid = value[-1]
        nid = int(nid)
        url = value[0]
        cover = value[1]
        title = value[2]
        author = value[3]
        score = value[4]
        score = float(score[0:-2])
        print(score)
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
        introduce = value[-2]
        # sql = "INSERT INTO " \
        #       "novel(nid,url,cover,title,author) " \
        #       "VALUES (%d,'%s','%s','%s','%s')" %(nid, url, cover, title, author)
        op1 = (nid, url, cover, title, author, score, type, depth, state, click_cnt, update_time, introduce)
        sql = """INSERT INTO 
        NOVEL(nid,url,cover,title,author,score,type,depth,state,click_cnt,update_time,introduce) 
        VALUES (%d,'%s','%s','%s','%s',%f,'%s',%s,'%s',%d,'%s','%s')""" % op1

        op2 = (nid, url, cover, title, author)
        cursor.execute(sql)
        print("success")
        # 提交到数据库执行
        conn.commit()
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql, op2)
        #     print("success")
        #     # 提交到数据库执行
        #     conn.commit()
        # except:
        #     # 如果发生错误则回滚
        #     print("failed")
        #     conn.rollback()


if __name__ == '__main__':
    novel_json_path = '../data/novel_3.json'
    ins_novel(novel_json_path)
    cursor.close()
    conn.close()
