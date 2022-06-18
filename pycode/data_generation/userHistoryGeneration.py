# -*- coding: gbk -*-
import random
from typing import MappingView


def generateHistory(userId: int):
    '''
    userData说明:
    list类型: [userId, {12:[3, 0.85], 45: [4, 0.40], ...}, {12:[3, 0.85], 45: [4, 0.40], ...}, ...]
    第一项是用户ID,第二、三、四项分别是动漫、漫画、小说记录（字典类型）
    作品评分: 满分5分,最低分1分,0分表示观看但未评分
    '''
    # data中存放用户数据，第一项是用户ID，第二、三、四项分别是动漫、漫画、小说记录（字典类型）
    userData = []
    userData.append(userId)
    animeTotalNum = 3531    # 动漫总数
    comicTotalNum = 20931   # 漫画总数
    novelTotalNum = 9841    # 小说总数
    # 动漫
    animeNum = int(3 + 20*(random.random()))            # 随机生成用户观看的数量
    animeDic = {}  # 用户观看的信息列表
    for i in range(animeNum):
        animeId = int(animeTotalNum * random.random())  # 作品编号
        animeMark = []  # [score, timePercentage]
        animeMark.append(int(random.random() * 6))      # 用户评分
        animeMark.append(round(random.random(), 2))     # 用户观看时长百分比
        animeDic[animeId] = animeMark
    userData.append(animeDic)
    # 漫画
    comicNum = int(3 + 20*(random.random()))
    comicDic = {}
    for i in range(comicNum):
        comicId = int(comicTotalNum * random.random())
        comicMark = []
        comicMark.append(int(random.random() * 6))      # 用户评分
        comicMark.append(round(random.random(), 2))     # 用户观看时长百分比
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # 小说
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelId = int(novelTotalNum * random.random())
        novelMark = []
        novelMark.append(int(random.random() * 6))      # 用户评分
        novelMark.append(round(random.random(), 2))     # 用户观看时长百分比
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    return userData

# 历史记录生成
usersTotalNum = 1000       # 用户总数
startUserId = 10000     # 起始用户ID
sysData = []   # 系统用户总数据: [userData[], userData[], ...]
for i in range(startUserId, startUserId + usersTotalNum):
    userData = generateHistory(i)
    sysData.append(userData)

print(sysData)
