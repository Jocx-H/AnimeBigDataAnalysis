# -*- coding = utf-8 -*-
# @Time :2022/6/24 15:08
# @File : userHistoryInsert.py
# @Author : derrick

import pymysql
import random
import time
from typing import MappingView
import json
import datetime
from dataGetAndProcess.data_generation import  getUserImgIdList as getList
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
usersTotalNum = 250     # 用户总数
startUserId = 1000      # 起始用户ID
tagSet = {}             # 用户画像对应的tag集合
userData = {}           # 单个用户数据列表
sysData = []            # 系统用户总数据 sysData = [userData1, userData2, ...]
recordList = []         # recordList = [[dailyRecord-user1], [dailyRecord-user2], ...]
initDate = datetime.datetime.now()
initDateStamp = int(initDate.timestamp() * 1000000)
db = None

# {1032: [{1138: [5, 0.26, True, True, 1656171745203046]}, {2788: [2, 0.3, False, True, 1656171745203046]}, {37016: [4, 0.95, True, False, 1656171745203046]}, {42: [0, 0.09, False, True, 1656171745203046]}]}
# {'message': 'insert init data successfully'}

# {1000: [{11432: [2, 0.15, False, False, 1656171859617069]}, {23060: [1, 0.15, False, True, 1656171859617069]}, {34005: [3, 0.93, False, False, 1656171859617069]}, {4139: [2, 0.56, False, False, 1656171859617069]}]}
# None

'''
根据用户id向数据库中插入初始数据（某一用户，每项单条）
'''
def insertInitData(userId: int):
    global db
    db = pymysql.connect(host="124.70.91.77", user="root", password="xxx", port=3306, database='AnimeBigDataAnalysis')
    # db = pymysql.connect(host="localhost", user="root", password="xxx", port=3307, database='ars')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    global userData
    userData = imgGer.initDataGenerate(userId)
    print(userData)
    uid = list(userData.keys())[0]
    # 动漫 anime
    aid = list(userData[userId][0].keys())[0] # [uid][1/2/3]
    a_markList = userData[userId][0][aid]
    a_score = a_markList[0]
    a_ratio = a_markList[1]
    a_like = a_markList[2]
    a_collect = a_markList[3]
    a_timestamp = a_markList[4]
    # 漫画 comic
    cid = list(userData[uid][1].keys())[0]  # [uid][1/2/3]
    c_markList = userData[uid][1][cid]
    c_score = c_markList[0]
    c_ratio = c_markList[1]
    c_like = c_markList[2]
    c_collect = c_markList[3]
    c_timestamp = c_markList[4]
    # 小说 novel
    nid = list(userData[uid][2].keys())[0]  # [uid][1/2/3]
    n_markList = userData[uid][2][nid]
    n_score = n_markList[0]
    n_ratio = n_markList[1]
    n_like = n_markList[2]
    n_collect = n_markList[3]
    n_timestamp = n_markList[4]
    # cosplay
    cosid = list(userData[uid][3].keys())[0]  # [uid][1/2/3]
    cos_markList = userData[uid][3][cosid]
    cos_score = cos_markList[0]
    cos_ratio = cos_markList[1]
    cos_like = cos_markList[2]
    cos_collect = cos_markList[3]
    cos_timestamp = cos_markList[4]
    userData = {}
    sql1 = """INSERT INTO useranimehistory(uid, aid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
           % (uid, aid, a_score, a_ratio, a_like, a_collect, a_timestamp)
    sql2 = """INSERT INTO usercomichistory(uid, cid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
           % (uid, cid, c_score, c_ratio, c_like, c_collect, c_timestamp)
    sql3 = """INSERT INTO usernovelhistory(uid, nid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
           % (uid, nid, n_score, n_ratio, n_like, n_collect, n_timestamp)
    sql4 = """INSERT INTO usercosplayhistory(uid, cosid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
           % (uid, cosid, cos_score, cos_ratio, cos_like, cos_collect, cos_timestamp)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        db.commit()
        # db.close()
        return {'message': 'insert init data successfully'}
    except:
        db.rollback()


'''
插入用户每日阅览记录
根据用户画像，以天为单位添加用户阅览记录。
ctrlCode: 控制码，0表示无特定画像的用户，1表示有画像的用户（中二、现充、肥宅、志怪、青春）
userId: 用户id
currDate: 插入日期
'''
def insertUserDailyData(ctrlCode: int, userId:int, currDate: int):
    global db
    db = pymysql.connect(host="124.70.91.77", user="root", password="xxx", port=3306, database='AnimeBigDataAnalysis')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    global preferenceRate
    preferFactor = 1  # 偏好因子：有偏好画像的用户对于特定的作品三连概率更高，以此修正
    if ctrlCode == 0:  # 无具体画像的用户无显著偏好，preferenceRate = 0
        preferenceRate = 0
    else:  # 有具体画像的用户阅览内容时有偏好，preferenceRate = 0.7(原始设置)，preferFactor = 1.5
        preferFactor = 1.5
    dailyRecordList = []  # 某用户record.py中的recordList，记录用户每天观看的各种类型作品的信息
    # userData = sysData[userId - 10000]
    # 动漫 - 每天有0.7的概率会看动漫
    dailyAnimeNum = int(random.random() * 5) if random.random() < animeDailyRate else 0
    for i in range(dailyAnimeNum):
        dailyRecordList.append(1)
        animeOptionList = ['1', str(int(animeTotalNum * random.random()))]
        animeOption1 = int(''.join(animeOptionList))  # 0.3
        animeOption2 = int(random.choice(animeSelectList))  # 0.7 - prefer
        dailyAnimeId = animeOption1 if random.random() > preferenceRate else animeOption2
        # dailyRecordList.append(dailyAnimeId == animeOption2) # -- 测试选项 --
        dailyAnimeMark = []
        animeScore = int(random.random() * 6)
        if animeScore < 5:
            animeScore += ctrlCode * 1  # 评分偏好
        dailyAnimeMark.append(animeScore)
        dailyAnimeMark.append(round(random.random(), 2))
        dailyAnimeMark.append((random.random() > 0.5 / preferFactor))  # 点赞
        dailyAnimeMark.append((random.random() > 0.5 / preferFactor))  # 收藏
        dailyAnimeMark.append(currDate)  # 日期
        # userData[userId][0][dailyAnimeId] = dailyAnimeMark
        sql1 = """INSERT INTO useranimehistory(uid, aid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (userId, dailyAnimeId, dailyAnimeMark[0], dailyAnimeMark[1], dailyAnimeMark[2], dailyAnimeMark[3], dailyAnimeMark[4])
        try:
            cursor.execute(sql1)
            db.commit()
            print({'message': 'daily anime successfully'})
        except:
            db.rollback()
            print({'message': 'daily anime fail'})
    # 漫画 - 每天有0.7的概率会看漫画
    dailyComicNum = int(random.random() * 5) if random.random() < comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyRecordList.append(2)
        comicOptionList = ['2', str(int(comicTotalNum * random.random()))]
        comicOption1 = int(''.join(comicOptionList))  # 0.3
        comicOption2 = int(random.choice(comicSelectList))  # 0.7 - prefer
        dailyComicId = comicOption1 if random.random() > preferenceRate else comicOption2
        # dailyRecordList.append(dailyComicId == comicOption2) # -- 测试选项 --
        dailyComicMark = []
        comicScore = int(random.random() * 6)
        if comicScore < 5:
            comicScore += ctrlCode * 1  # 评分偏好
        dailyComicMark.append(comicScore)
        dailyComicMark.append(round(random.random(), 2))
        dailyComicMark.append((random.random() > 0.5 / preferFactor))  # 点赞
        dailyComicMark.append((random.random() > 0.5 / preferFactor))  # 收藏
        dailyComicMark.append(currDate)  # 日期
        # userData[userId][1][dailyComicId] = dailyComicMark
        sql2 = """INSERT INTO usercomichistory(uid, cid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (userId, dailyComicId, dailyComicMark[0], dailyComicMark[1], dailyComicMark[2], dailyComicMark[3], dailyComicMark[4])
        try:
            cursor.execute(sql2)
            db.commit()
            print({'message': 'daily comic successfully'})
        except:
            db.rollback()
            print({'message': 'daily comic fail'})
    # 小说 - 每天有0.7的概率会看小说
    dailyNovelNum = int(random.random() * 5) if random.random() < novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyRecordList.append(3)
        novelOptionList = ['3', str(int(novelTotalNum * random.random()))]
        novelOption1 = int(''.join(novelOptionList))  # 0.3
        novelOption2 = int(random.choice(novelSelectList))  # 0.7 - prefer
        dailyNovelId = novelOption1 if random.random() > preferenceRate else novelOption2
        # dailyRecordList.append(dailyNovelId == novelOption2) # -- 测试选项 --
        dailyNovelMark = []
        novelScore = int(random.random() * 6)
        if novelScore < 5:
            novelScore += ctrlCode * 1  # 评分偏好
        dailyNovelMark.append(novelScore)
        dailyNovelMark.append(round(random.random(), 2))
        dailyNovelMark.append((random.random() > 0.5 / preferFactor))  # 点赞
        dailyNovelMark.append((random.random() > 0.5 / preferFactor))  # 收藏
        dailyNovelMark.append(currDate)  # 日期
        # userData[userId][2][dailyNovelId] = dailyNovelMark
        sql3 = """INSERT INTO usernovelhistory(uid, nid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (userId, dailyNovelId, dailyNovelMark[0], dailyNovelMark[1], dailyNovelMark[2], dailyNovelMark[3], dailyNovelMark[4])
        try:
            cursor.execute(sql3)
            db.commit()
            print({'message': 'daily novel successfully'})
        except:
            db.rollback()
            print({'message': 'daily novel fail'})
    # cosplay - 每天有0.25的概率会看cosplay
    dailyCosNum = int(random.random() * 5) if random.random() < cosDailyRate else 0
    for i in range(dailyCosNum):
        dailyRecordList.append(4)
        cosOptionList = ['4', str(int(cosTotalNum * random.random()))]
        cosOption1 = int(''.join(cosOptionList))  # 0.3
        cosOption2 = int(random.choice(cosSelectList))  # 0.7 - prefer
        dailyCosId = cosOption1 if random.random() > preferenceRate else cosOption2
        # dailyRecordList.append(dailyCosId == cosOption2) # -- 测试选项 --
        dailyCosMark = []
        cosScore = int(random.random() * 6)
        if cosScore < 5:
            cosScore += ctrlCode * 1  # 评分偏好
        dailyCosMark.append(cosScore)
        dailyCosMark.append(round(random.random(), 2))
        dailyCosMark.append((random.random() > 0.5 / preferFactor))  # 点赞
        dailyCosMark.append((random.random() > 0.5 / preferFactor))  # 收藏
        dailyCosMark.append(currDate)  # 日期
        # userData[userId][3][dailyCosId] = dailyCosMark
        sql4 = """INSERT INTO usercosplayhistory(uid, cosid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (userId, dailyCosId, dailyCosMark[0], dailyCosMark[1], dailyCosMark[2], dailyCosMark[3], dailyCosMark[4])
        try:
            cursor.execute(sql4)
            db.commit()
            print({'message': 'daily cosplay successfully'})
        except:
            db.rollback()
            print({'message': 'daily cosplay fail'})


'''
设定用户的画像
'''
def setUserImg(type: str):
    tagSet = {}
    if type == 'zhonger':       # 中二
        tagSet = getList.zhongerTagSet
    elif type == 'xianchong':   # 现充
        tagSet = getList.xianchongTagSet
    elif type == 'feizhai':     # 肥宅
        tagSet = getList.feizhaiTagSet
    elif type == 'zhiguai':     # 志怪
        tagSet = getList.zhiguaiTagSet
    elif type == 'qingchun':    # 青春
        tagSet = getList.qingchunTagSet
    global animeSelectList, comicSelectList, novelSelectList, cosSelectList
    # 读取已经保存的各个画像对应的selectList：空间换时间
    jsonPath = "../data_generation/" + type + "SelectList.json"
    jsonFile = open(jsonPath, 'r')
    selectList = json.load(jsonFile)
    animeSelectList = selectList[0]
    comicSelectList = selectList[1]
    novelSelectList = selectList[2]
    cosSelectList = selectList[3]


'''main'''
if __name__ == "__main__":
    # 插入初始数据
    for i in range(startUserId, startUserId + usersTotalNum):
        print(insertInitData(i))
    # 插入每日阅览记录
    timeDateForm = initDate
    time.sleep(0.001)
    for day in range(1, 5):               # 日期遍历（eg：更新4天的阅览记录）
        currDateForm = timeDateForm - day * datetime.timedelta(days=1)
        currDate = int(currDateForm.timestamp() * 1000000)
        for i in range(startUserId, startUserId + usersTotalNum):
            if i <= 1100 and i % 20 == 0:
                print("new type start")
            if i in range(1000, 1020):  # 中二
                setUserImg('zhonger')
                insertUserDailyData(1, i, currDate)
            elif i in range(1020, 1040):  # 现充
                setUserImg('xianchong')
                insertUserDailyData(1, i, currDate)
            elif i in range(1040, 1060):  # 肥宅
                setUserImg('feizhai')
                insertUserDailyData(1, i, currDate)
            elif i in range(1060, 1080):  # 志怪
                setUserImg('zhiguai')
                insertUserDailyData(1, i, currDate)
            elif i in range(1080, 1100):  # 青春
                setUserImg('qingchun')
                insertUserDailyData(1, i, currDate)
            else:                           # 无特定画像
                insertUserDailyData(0, i, currDate)
    print('generate completed!')
    # 关闭数据库连接
    db.close()
    print('db closed.')