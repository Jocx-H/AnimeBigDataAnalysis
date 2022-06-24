# -*- coding = utf-8 -*-
# @Time :2022/6/24 15:08
# @File : userHistoryDao.py
# @Author : derrick

import pymysql
import random
import time
from typing import MappingView
import json
import datetime
from dataGetAndProcess.data_generation import getUserImgIdList as getList
from dataGetAndProcess.data_generation import imgBasedHistoryGeneration as imgGer

'''
将用户初始数据和每日阅览数据加入数据库
相关操作：insert
'''

# 各类作品总数
animeTotalNum = 3511    # 动漫总数
comicTotalNum = 20931   # 漫画总数
novelTotalNum = 9841    # 小说总数
cosTotalNum = 200       # cosplay 总数
# 每天阅览动漫、漫画、小说、cosplay的概率
animeDailyRate = 0.7
comicDailyRate = 0.7
novelDailyRate = 0.7
cosDailyRate = 0.25
# 用户画像阅览偏好：选择画像内作品的概率
preferenceRate = 0.7
# 存储不同画像的用户偏好作品的id list
animeSelectList = []
comicSelectList = []
novelSelectList = []
cosSelectList = []
# 全局变量信息设置
usersTotalNum = 15    # 用户总数
startUserId = 10000     # 起始用户ID
tagSet = {}             # 用户画像对应的tag集合
userData = {}           # 单个用户数据列表
sysData = []            # 系统用户总数据 sysData = [userData1, userData2, ...]
recordList = []         # recordList = [[dailyRecord-user1], [dailyRecord-user2], ...]
initDate = datetime.datetime.now()
initDateStamp = int(initDate.timestamp() * 1000000)


def insertAnimeInitData(userId: int):
    userData = imgGer.initDataGenerate(userId)
    uid = list(userData.keys())[0]
    aid = list(userData[userId][0].key())[0]
    markList = userData[userId][0][aid]
    score = markList[0]
    ratio = markList[1]
    like = markList[2]
    collect = markList[3]
    timestamp = markList[4]
    db = pymysql.connect(host="localhost", user="root", password="12345", database="ars")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = """INSERT INTO userAnimeHistoty(uid, aid, score, ratio, like, collect, timestamp) VALUES (%d,%d,%d,%f,%f,%d,%d,%d)""" \
          % (uid, aid, score, ratio, like, collect, timestamp)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()
        return {'message': 'successfully'}
    except:
        db.rollback()