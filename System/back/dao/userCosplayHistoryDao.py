#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx, derrick,WILLOSCAR
@Description:
'''

import pymysql
from bean.userCosplayHistoryBean import UserCosplayHistoryBean
from dao.utils import database

'''
根据用户id获取其所有的cosplay阅览记录
返回格式：
[{'coshid': 1, 'uid': 10000, 'cosid': 11, 'score': 1.0, 'ratio': 0.32, 'thumb': 1, 'collect': 0, 'time': xxx}, {..}]
'''


def getCosplayHistoryByUserId(userId: int):
    db, cursor = database()
    sql = """SELECT * FROM usercosplayhistory WHERE uid = %d""" % (userId)
    try:
        cursor.execute(sql)
        tmp_result = cursor.fetchall()
        db.commit()
        db.close()
        result = []
        for row in tmp_result:
            result.append(
                UserCosplayHistoryBean(
                    coshid=row[0],
                    uid=row[1],
                    cosid=row[2],
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
        return {'message': 'get cosplay fail'}


# print(getCosplayHistoryByUserId(10001))


'''
返回usercosplayhistroy中全部用户阅览数据
数据量大，谨慎操作！
'''


def getCosplayHistoryAll():
    db, cursor = database()
    sql = """SELECT * FROM usercosplayhistory"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
    except:
        db.rollback()
        return {'message': 'get cosplay fail'}

# print(getCosplayHistoryAll())
