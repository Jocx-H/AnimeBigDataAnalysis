# -*- coding: gbk -*-
import random
import time
from typing import MappingView
import json

'''
userHistoryGeneration.py
包含功能：
1.生成用户历史；
2.每日阅览记录。
'''

# 各类作品总数
animeTotalNum = 3531    # 动漫总数
comicTotalNum = 20931   # 漫画总数
novelTotalNum = 9841    # 小说总数
cosTotalNum = 200       # cosplay 总数
# 每天 不 阅览动漫、漫画、小说的概率
animeDailyRate = 0.3
comicDailyRate = 0.3
novelDailyRate = 0.3
cosDailyRate = 0.5
# 全局变量信息设置
usersTotalNum = 3    # 用户总数
startUserId = 10000     # 起始用户ID
userData = []           # 单个用户数据列表
sysData = []            # 系统用户总数据: [userData[], userData[], ...]

'''生成单个用户历史（基础创建）'''
def generateHistory(userId: int):
    # userData说明:
    # list类型: [userId, {12:[3, 0.85, 1, 0], 45: [4, 0.40, 0, 1], ...}, {12:[3, 0.85, 0, 0], 45: [4, 0.40, 1, 1], ...}, ...]
    # 第一项是用户ID,第二、三、四、五项分别是动漫、漫画、小说、cosplay记录（字典类型）
    # 作品评分: 满分5分,最低分1分,0分表示观看但未评分
    # mark列表中存放莫用户作品的观看信息，由评分(int)、观看时长占总时长占比(float)、点赞(bool)、收藏(bool)构成：[score, timePercentage, like, collect]
    userData = []
    userData.append(userId)
    # 动漫 作品编号1开头
    animeNum = int(3 + 20*(random.random()))            # 随机生成用户观看的数量
    animeDic = {}  # 用户观看的信息列表
    for i in range(animeNum):
        animeIdList = ['1', str(int(animeTotalNum * random.random()))]
        animeId = int(''.join(animeIdList))             # 作品编号
        animeMark = []                                  # [score, timePercentage]
        animeMark.append(int(random.random() * 6))      # 用户评分
        animeMark.append(round(random.random(), 2))     # 用户观看时长百分比
        animeMark.append((random.random() > 0.5))       # 点赞
        animeMark.append((random.random() > 0.5))       # 收藏
        animeDic[animeId] = animeMark
    userData.append(animeDic)
    # 漫画 作品编号2开头
    comicNum = int(3 + 20*(random.random()))
    comicDic = {}
    for i in range(comicNum):
        comicIdList = ['2', str(int(comicTotalNum * random.random()))]
        comicId = int(''.join(comicIdList))             # 作品编号
        comicMark = []
        comicMark.append(int(random.random() * 6))      # 用户评分
        comicMark.append(round(random.random(), 2))     # 用户观看时长百分比
        comicMark.append((random.random() > 0.5))       # 点赞
        comicMark.append((random.random() > 0.5))       # 收藏
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # 小说 作品编号3开头
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelIdList = ['3', str(int(novelTotalNum * random.random()))]
        novelId = int(''.join(novelIdList))             # 作品编号
        novelMark = []
        novelMark.append(int(random.random() * 6))      # 用户评分
        novelMark.append(round(random.random(), 2))     # 用户观看时长百分比
        novelMark.append((random.random() > 0.5))       # 点赞
        novelMark.append((random.random() > 0.5))       # 收藏
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    # cosplay 作品编号4开头
    cosNum = int(3 + 20 * (random.random()))
    cosDic = {}
    for i in range(cosNum):
        cosIdList = ['3', str(int(cosTotalNum * random.random()))]
        cosId = int(''.join(cosIdList))  # 作品编号
        cosMark = []
        cosMark.append(int(random.random() * 6))        # 用户评分
        cosMark.append(round(random.random(), 2))       # 用户观看时长百分比
        cosMark.append((random.random() > 0.5))         # 点赞
        cosMark.append((random.random() > 0.5))         # 收藏
        cosDic[cosId] = cosMark
    userData.append(cosDic)
    return userData

'''生成每日阅览记录（添加）'''
def generateDailyBrowsing(userData: list):
    dailyRecordList = []  # 用户record.py中的recordList，记录用户每天观看的各种类型作品的信息
    # 动漫
    dailyAnimeNum = int(random.random() * 5) if random.random() > animeDailyRate else 0
    for i in range(dailyAnimeNum):
        dailyRecordList.append(1)
        dailyAnimeIdList = ['1', str(int(animeTotalNum * random.random()))]
        dailyAnimeId = int(''.join(dailyAnimeIdList))
        dailyAnimeMark = []
        dailyAnimeMark.append(int(random.random() * 6))
        dailyAnimeMark.append(round(random.random(), 2))
        dailyAnimeMark.append((random.random() > 0.5))  # 点赞
        dailyAnimeMark.append((random.random() > 0.5))  # 收藏
        userData[1][dailyAnimeId] = dailyAnimeMark
    # 漫画
    time.sleep(0.01)
    dailyComicNum = int(random.random() * 5) if random.random() > comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyRecordList.append(2)
        dailyComicIdList = ['2', str(int(comicTotalNum * random.random()))]
        dailyComicId = int(''.join(dailyComicIdList))
        dailyComicMark = []
        dailyComicMark.append(int(random.random() * 6))
        dailyComicMark.append(round(random.random(), 2))
        dailyComicMark.append((random.random() > 0.5))  # 点赞
        dailyComicMark.append((random.random() > 0.5))  # 收藏
        userData[2][dailyComicId] = dailyComicMark
    # 小说
    time.sleep(0.01)
    dailyNovelNum = int(random.random() * 5) if random.random() > novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyRecordList.append(3)
        dailyNovelIdList = ['3', str(int(novelTotalNum * random.random()))]
        dailyNovelId = int(''.join(dailyNovelIdList))
        dailyNovelMark = []
        dailyNovelMark.append(int(random.random() * 6))
        dailyNovelMark.append(round(random.random(), 2))
        dailyNovelMark.append((random.random() > 0.5))  # 点赞
        dailyNovelMark.append((random.random() > 0.5))  # 收藏
        userData[3][dailyNovelId] = dailyNovelMark
    # cosplay
    time.sleep(0.01)
    dailyCosNum = int(random.random() * 5) if random.random() > cosDailyRate else 0
    for i in range(dailyCosNum):
        dailyRecordList.append(4)
        dailyCosIdList = ['3', str(int(cosTotalNum * random.random()))]
        dailyCosId = int(''.join(dailyCosIdList))
        dailyCosMark = []
        dailyCosMark.append(int(random.random() * 6))
        dailyCosMark.append(round(random.random(), 2))
        dailyCosMark.append((random.random() > 0.5))  # 点赞
        dailyCosMark.append((random.random() > 0.5))  # 收藏
        userData[4][dailyCosId] = dailyCosMark
    return userData, dailyRecordList


# 测试代码
for i in range(startUserId, startUserId + usersTotalNum):
    userData = generateHistory(i)
    sysData.append(userData)

print(sysData)
print("\n")

time.sleep(0.3)
recordList = []
for item in sysData:
    recordList = generateDailyBrowsing(item)[1]
print(sysData)
print(recordList)

# with open("sysData.json", "w", encoding='utf-8') as f:
#     # json.dump(dict_, f)  # 写为一行
#     json.dump(sysData, f, indent = 2, sort_keys = True, ensure_ascii = False)  # 写为多行