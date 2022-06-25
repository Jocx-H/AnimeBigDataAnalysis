#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx, derrick
@Description:
'''

import pymysql

'''
根据用户id获取其所有的漫画阅览记录
返回格式：
[{'chid': 1, 'uid': 10000, 'cid': 11, 'score': 1.0, 'ratio': 0.32, 'thumb': 1, 'collect': 0, 'time': xxx}, {..}]
'''
def getComicHistoryByUserId(userId: int):
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM usercomichistory WHERE uid = %d"""%(userId)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get comic fail'}

# print(getComicHistoryByUserId(10001))


'''
返回usercomichistroy中全部用户阅览数据
数据量大，谨慎操作！
'''
def getComicHistoryAll():
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM usercomichistory"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get comic fail'}

# print(getComicHistoryAll())