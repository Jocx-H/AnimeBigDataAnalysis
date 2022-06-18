# -*- coding: gbk -*-
import random
import time
from typing import MappingView

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
# 每天阅览动漫、漫画、小说的概率
animeDailyRate = 0.5
comicDailyRate = 0.7
novelDailyRate = 0.7
# 全局变量信息设置
usersTotalNum = 3    # 用户总数
startUserId = 10000     # 起始用户ID
userData = []           # 单个用户数据列表
sysData = []            # 系统用户总数据: [userData[], userData[], ...]

'''生成单个用户历史（基础创建）'''
def generateHistory(userId: int):
    # userData说明:
    # list类型: [userId, {12:[3, 0.85], 45: [4, 0.40], ...}, {12:[3, 0.85], 45: [4, 0.40], ...}, ...]
    # 第一项是用户ID,第二、三、四项分别是动漫、漫画、小说记录（字典类型）
    # 作品评分: 满分5分,最低分1分,0分表示观看但未评分
    # mark列表中存放莫用户作品的观看信息，由评分和观看时长占总时长占比构成：[score, timePercentage]
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
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # 小说 作品编号3开头
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelIdList = ['3', str(int(novelTotalNum * random.random()))]
        novelId = int(''.join(comicIdList))             # 作品编号
        novelMark = []
        novelMark.append(int(random.random() * 6))      # 用户评分
        novelMark.append(round(random.random(), 2))     # 用户观看时长百分比
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    return userData

'''生成每日阅览记录（添加）'''
def generateDailyBrowsing(userData: list):
    # 动漫
    dailyAnimeNum = int(random.random() * 5) if random.random() > animeDailyRate else 0
    for i in range(dailyAnimeNum):
        dailyAnimeIdList = ['1', str(int(animeTotalNum * random.random()))]
        dailyAnimeId = int(''.join(dailyAnimeIdList))
        dailyAnimeMark = []
        dailyAnimeMark.append(int(random.random() * 6))
        dailyAnimeMark.append(round(random.random(), 2))
        userData[1][dailyAnimeId] = dailyAnimeMark
    # 漫画
    dailyComicNum = int(random.random() * 5) if random.random() > comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyComicIdList = ['2', str(int(comicTotalNum * random.random()))]
        dailyComicId = int(''.join(dailyComicIdList))
        dailyComicMark = []
        dailyComicMark.append(int(random.random() * 6))
        dailyComicMark.append(round(random.random(), 2))
        userData[2][dailyComicId] = dailyComicMark
    # 小说
    dailyNovelNum = int(random.random() * 5) if random.random() > novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyNovelIdList = ['3', str(int(novelTotalNum * random.random()))]
        dailyNovelId = int(''.join(dailyNovelIdList))
        dailyNovelMark = []
        dailyNovelMark.append(int(random.random() * 6))
        dailyNovelMark.append(round(random.random(), 2))
        userData[3][dailyNovelId] = dailyNovelMark
    return userData


# 测试代码
for i in range(startUserId, startUserId + usersTotalNum):
    userData = generateHistory(i)
    sysData.append(userData)

print(sysData)
print("\n")

time.sleep(3)

for item in sysData:
    generateDailyBrowsing(item)
print(sysData)