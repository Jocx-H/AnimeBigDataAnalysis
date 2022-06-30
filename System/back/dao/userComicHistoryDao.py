#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx, derrick, CloudAndMist
@Description:
'''

import pymysql
from bean.userComicHistoryBean import UserComicHistoryBean
from dao.utils import database


def getComicHistoryByUserId(userId: int):
    """
    根据用户id获取其所有的漫画阅览记录
    返回格式：
    [{'chid': 1, 'uid': 10000, 'cid': 11, 'score': 1.0, 'ratio': 0.32, 'thumb': 1, 'collect': 0, 'time': xxx}, {..}]
    """
    db, cursor = database()
    sql = """SELECT * FROM usercomichistory WHERE uid = %d"""%(userId)
    try:
        cursor.execute(sql)
        tmp_result = cursor.fetchall()
        db.commit()
        db.close()
        result = []
        for row in tmp_result:
            result.append(
                UserComicHistoryBean(
                    chid=row[0],
                    uid=row[1],
                    cid=row[2],
                    score=row[3],
                    ratio=row[4],
                    like=row[5],
                    collect=row[6],
                    timestamp=row[7]
                )
            )
        return result
    except:
        db.rollback()
        return {'message': 'get comic fail'}


def getComicHistoryAll():
    """
    返回usercomichistroy中全部用户阅览数据
    数据量大，谨慎操作！
    """
    db, cursor = database()
    sql = """SELECT * FROM usercomichistory"""
    try:
        cursor.execute(sql)
        tmp_result = cursor.fetchall()
        db.commit()
        db.close()
        result = []
        for row in tmp_result:
            result.append(
                UserComicHistoryBean(
                    chid=row[0],
                    uid=row[1],
                    cid=row[2],
                    score=row[3],
                    ratio=row[4],
                    like=row[5],
                    collect=row[6],
                    timestamp=row[7]
                )
            )
        return result
    except:
        db.rollback()
        return {'message': 'get comic fail'}
