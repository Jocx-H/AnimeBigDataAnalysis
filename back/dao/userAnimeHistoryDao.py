#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx, derrick
@Description:
'''

import pymysql

'''
根据用户id获取其所有的动漫阅览记录
返回格式：
[{'ahid': 1, 'uid': 10000, 'aid': 11, 'score': 1.0, 'ratio': 0.32, 'thumb': 1, 'collect': 0, 'time': xxx}, {..}]
'''
def getAnimeHistoryByUserId(userId: int):
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM useranimehistory WHERE uid = %d"""%(userId)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get anime fail'}

# print(getAnimeHistoryByUserId(10001))


'''
返回useranimehistroy中全部用户阅览数据
数据量大，谨慎操作！
'''
def getAnimeHistoryAll():
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM useranimehistory"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get anime fail'}

# print(getAnimeHistoryAll())