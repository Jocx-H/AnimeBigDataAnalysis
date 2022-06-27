#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx, derrick,WILLOSCAR
@Description:
'''

import pymysql
from bean.userNovelHistoryBean import UserNovelHistoryBean

'''
根据用户id获取其所有的动漫阅览记录
返回格式：
[{'nhid': 1, 'uid': 10000, 'nid': 11, 'score': 1.0, 'ratio': 0.32, 'thumb': 1, 'collect': 0, 'time': xxx}, {..}]
'''


def getNovelHistoryByUserId(userId: int):
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM usernovelhistory WHERE uid = %d""" % (userId)
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        novelList = UserNovelHistoryBean(
            nhid=row[0],
            uid=row[1],
            nid=row[2],
            score=row[3],
            ratio=row[4],
            like=row[5],
            collect=row[6],
            timestamp=row[7]
        )
        db.commit()
        db.close()
        return novelList
    except:
        db.rollback()
        return {'message': 'get novel fail'}


# print(getNovelHistoryByUserId(10001))


'''
返回usernovelhistroy中全部用户阅览数据
数据量大，谨慎操作！
'''


def getNovelHistoryAll():
    db = pymysql.connect(host="localhost", user="root", password="xxxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT * FROM usernovelhistory"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get novel fail'}

# print(getNovelHistoryAll())
