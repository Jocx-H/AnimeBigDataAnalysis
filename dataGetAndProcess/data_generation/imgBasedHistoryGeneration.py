# -*- coding = utf-8 -*-
# @Time :2022/6/23 18:51
# @File : imgBasedHistoryGeneration.py
# @author: derrick

from dataGetAndProcess.data_generation import getUserImgIdList as getList
import random
import time
from typing import MappingView
import json
import datetime


'''
imgBasedHistoryGeneration.py
功能：依据用户画像的用户记录生成
有两种模式：无特定画像的用户记录生成、有特定画像的用户记录生成
后者的用户画像包括：中二、现充、肥宅、志怪、青春五种
'''


# 各类作品总数
animeTotalNum = 3512    # 动漫总数
comicTotalNum = 20931   # 漫画总数
novelTotalNum = 9841    # 小说总数
cosTotalNum = 200       # cosplay 总数
# 每天阅览动漫、漫画、小说、cosplay的概率
animeDailyRate = 0.7
comicDailyRate = 0.7
novelDailyRate = 0.7
cosDailyRate = 0.25
# 用户画像阅览偏好：选择画像内作品的概率
preferenceRate = 0.8
# 存储不同画像的用户偏好作品的id list
animeSelectList = []
comicSelectList = []
novelSelectList = []
cosSelectList = []
# 独占作品列表
animeUniqueImgList = []
comicUniqueImgList = []
novelUniqueImgList = []
cosUniqueImgList = []
# 全局变量信息设置
usersTotalNum = 200     # 用户总数
startUserId = 1000      # 起始用户ID
tagSet = {}             # 用户画像对应的tag集合
userData = {}           # 单个用户数据列表
sysData = []            # 系统用户总数据 sysData = [userData1, userData2, ...]
recordList = []         # recordList = [[dailyRecord-user1], [dailyRecord-user2], ...]
initDate = datetime.datetime.now()
initDateStamp = int(initDate.timestamp() * 1000000)

'''
根据用户id进行初始数据生成（某个用户，init为每项单条）
'''
def initDataGenerate(userId: int) -> dict:
    initSysData = []
    userData = {}           # userData = {userId: [userHistoryList]}
    userHistoryList = []    # userHistoryList = [{animeDic}, {comicDic}]
    # 动漫 作品编号1开头
    animeDic = {}
    animeIdList = ['1', str(1 + int(animeTotalNum * random.random()))]
    animeId = int(''.join(animeIdList))             # 作品编号
    animeMark = []                                  # [评分, 时间占比, 点赞, 收藏, 日期]
    animeMark.append(int(random.random() * 6))      # 用户评分
    animeMark.append(round(random.random(), 2))     # 用户观看时长百分比
    animeMark.append((random.random() > 0.5))       # 点赞（bool）
    animeMark.append((random.random() > 0.5))       # 收藏（bool）
    animeMark.append(initDateStamp)                 # 日期（date）
    animeDic[animeId] = animeMark
    userHistoryList.append(animeDic)
    # 漫画 作品编号2开头
    comicDic = {}
    comicIdList = ['2', str(1 + int(comicTotalNum * random.random()))]
    comicId = int(''.join(comicIdList))  # 作品编号
    comicMark = []                                  # [评分, 时间占比, 点赞, 收藏, 日期]
    comicMark.append(int(random.random() * 6))      # 用户评分
    comicMark.append(round(random.random(), 2))     # 用户观看时长百分比
    comicMark.append((random.random() > 0.5))       # 点赞（bool）
    comicMark.append((random.random() > 0.5))       # 收藏（bool）
    comicMark.append(initDateStamp)                 # 日期（date）
    comicDic[comicId] = comicMark
    userHistoryList.append(comicDic)
    # 小说 作品编号3开头
    novelDic = {}
    novelIdList = ['3', str(1 + int(novelTotalNum * random.random()))]
    novelId = int(''.join(novelIdList))             # 作品编号
    novelMark = []                                  # [评分, 时间占比, 点赞, 收藏, 日期]
    novelMark.append(int(random.random() * 6))      # 用户评分
    novelMark.append(round(random.random(), 2))     # 用户观看时长百分比
    novelMark.append((random.random() > 0.5))       # 点赞（bool）
    novelMark.append((random.random() > 0.5))       # 收藏（bool）
    novelMark.append(initDateStamp)                 # 日期（date）
    novelDic[novelId] = novelMark
    userHistoryList.append(novelDic)
    # cosplay 作品编号4开头
    cosDic = {}
    cosIdList = ['4', str(1 + int(cosTotalNum * random.random()))]
    cosId = int(''.join(cosIdList))                 # 作品编号
    cosMark = []                                    # [评分, 时间占比, 点赞, 收藏, 日期]
    cosMark.append(int(random.random() * 6))        # 用户评分
    cosMark.append(round(random.random(), 2))       # 用户观看时长百分比
    cosMark.append((random.random() > 0.5))         # 点赞（bool）
    cosMark.append((random.random() > 0.5))         # 收藏（bool）
    cosMark.append(initDateStamp)                   # 日期（date）
    cosDic[cosId] = cosMark
    userHistoryList.append(cosDic)
    # userData
    userData[userId] = userHistoryList
    return userData


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
    global animeUniqueImgList, comicUniqueImgList, novelUniqueImgList
    # 读取已经保存的各个画像对应的selectList：空间换时间
    jsonPath = type + "SelectList.json"
    jsonFile = open(jsonPath, 'r')
    selectList = json.load(jsonFile)
    animeSelectList = selectList[0]
    comicSelectList = selectList[1]
    novelSelectList = selectList[2]
    cosSelectList = selectList[3]
    uniquePath = type + "UniqueIdList.json"
    uniqueFile = open(uniquePath, 'r')
    uniqueList = json.load(uniqueFile)
    animeUniqueImgList = uniqueList[0]
    comicUniqueImgList = uniqueList[1]
    novelUniqueImgList = uniqueList[2]


'''
基于用户画像的记录生成函数：
根据用户画像，以天为单位添加用户阅览记录。
ctrlCode: 控制码，0表示无特定画像的用户，1表示有画像的用户（中二、现充、肥宅、志怪、青春）
userId: 用户id
currDate: 插入日期
'''
def imgDailyGenerate(ctrlCode: int, userId: int, currDate: int):
    global preferenceRate
    preferFactor = 1        # 偏好因子：有偏好画像的用户对于特定的作品三连概率更高，以此修正
    if ctrlCode == 0:       # 无具体画像的用户无显著偏好，preferenceRate = 0
        preferenceRate = 0
        print('wuhuaxiang')
        print(animeSelectList)
    else:                   # 有具体画像的用户阅览内容时有偏好，preferenceRate = 0.7(原始设置)，preferFactor = 1.5
        preferFactor = 1.5
    dailyRecordList = []    # 某用户record.py中的recordList，记录用户每天观看的各种类型作品的信息
    userData = sysData[userId-1000]
    # 动漫 - 每天有0.7的概率会看动漫
    dailyAnimeNum = int(random.random() * 5) if random.random() < animeDailyRate else 0
    for animeIndex in range(dailyAnimeNum):
        dailyRecordList.append(1)
        animeOptionList = ['1', str(1 + int(animeTotalNum * random.random()))]
        animeOption1 = int(''.join(animeOptionList))        # not prefer
        if len(animeUniqueImgList) > 0:
            # print(animeUniqueImgList)
            animeOption3 = int(random.choice(animeUniqueImgList))
            animeOption4 = int(random.choice(animeSelectList))
            animeOption2 = animeOption4 if random.random() > preferenceRate else animeOption3  # prefer
        else:
            animeOption2 = int(random.choice(animeSelectList))
        dailyAnimeId = animeOption1 if random.random() > preferenceRate else animeOption2
        # dailyRecordList.append(dailyAnimeId == animeOption2) # -- 测试选项 --
        dailyAnimeMark = []
        animeScore = int(random.random() * 6)
        if animeScore < 5:
            animeScore += ctrlCode * 1 # 评分偏好
        dailyAnimeMark.append(animeScore)
        dailyAnimeMark.append(min(round(random.random() * preferFactor, 2), 1))
        dailyAnimeMark.append((random.random() > 0.5 / preferFactor))   # 点赞
        dailyAnimeMark.append((random.random() > 0.5 / preferFactor))   # 收藏
        dailyAnimeMark.append(currDate)                                 # 日期
        userData[userId][0][dailyAnimeId] = dailyAnimeMark
    # 漫画 - 每天有0.7的概率会看漫画
    dailyComicNum = int(random.random() * 5) if random.random() < comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyRecordList.append(2)
        comicOptionList = ['2', str(1 + int(comicTotalNum * random.random()))]
        comicOption1 = int(''.join(comicOptionList))        # not prefer
        # comicOption2 = int(random.choice(comicSelectList))  # prefer
        if len(comicUniqueImgList) > 0:
            comicOption3 = int(random.choice(comicUniqueImgList))
            comicOption2 = int(random.choice(comicSelectList)) if random.random() > preferenceRate else comicOption3  # prefer
        else:
            comicOption2 = int(random.choice(comicSelectList))
        dailyComicId = comicOption1 if random.random() > preferenceRate else comicOption2
        # dailyRecordList.append(dailyComicId == comicOption2) # -- 测试选项 --
        dailyComicMark = []
        comicScore = int(random.random() * 6)
        if comicScore < 5:
            comicScore += ctrlCode * 1  # 评分偏好
        dailyComicMark.append(comicScore)
        dailyComicMark.append(min(round(random.random() * preferFactor, 2), 1))
        dailyComicMark.append((random.random() > 0.5 / preferFactor))   # 点赞
        dailyComicMark.append((random.random() > 0.5 / preferFactor))   # 收藏
        dailyComicMark.append(currDate)                                 # 日期
        userData[userId][1][dailyComicId] = dailyComicMark
    # 小说 - 每天有0.7的概率会看小说
    dailyNovelNum = int(random.random() * 5) if random.random() < novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyRecordList.append(3)
        novelOptionList = ['3', str(1 + int(novelTotalNum * random.random()))]
        novelOption1 = int(''.join(novelOptionList))        # not prefer
        # novelOption2 = int(random.choice(novelSelectList))  # prefer
        if len(novelUniqueImgList) > 0:
            novelOption3 = int(random.choice(novelUniqueImgList))
            novelOption4 = int(random.choice(novelSelectList))
            novelOption2 = novelOption4 if random.random() > preferenceRate else novelOption3  # prefer
        else:
            novelOption2 = int(random.choice(novelSelectList))
        dailyNovelId = novelOption1 if random.random() > preferenceRate else novelOption2
        # dailyRecordList.append(dailyNovelId == novelOption3) # -- 测试选项 --
        dailyNovelMark = []
        novelScore = int(random.random() * 6)
        if novelScore < 5:
            novelScore += ctrlCode * 1  # 评分偏好
        dailyNovelMark.append(novelScore)
        dailyNovelMark.append(min(round(random.random() * preferFactor, 2), 1))
        dailyNovelMark.append((random.random() > 0.5 / preferFactor))   # 点赞
        dailyNovelMark.append((random.random() > 0.5 / preferFactor))   # 收藏
        dailyNovelMark.append(currDate)                                 # 日期
        userData[userId][2][dailyNovelId] = dailyNovelMark
    # cosplay - 每天有0.25的概率会看cosplay
    dailyCosNum = int(random.random() * 5) if random.random() < cosDailyRate else 0
    for i in range(dailyCosNum):
        dailyRecordList.append(4)
        cosOptionList = ['4', str(1 + int(cosTotalNum * random.random()))]
        cosOption1 = int(''.join(cosOptionList))        # 0.3
        cosOption2 = int(random.choice(cosSelectList))  # 0.7 - prefer
        dailyCosId = cosOption1 if random.random() > preferenceRate else cosOption2
        # dailyRecordList.append(dailyCosId == cosOption2) # -- 测试选项 --
        dailyCosMark = []
        cosScore = int(random.random() * 6)
        if cosScore < 5:
            cosScore += ctrlCode * 1  # 评分偏好
        dailyCosMark.append(cosScore)
        dailyCosMark.append(min(round(random.random() * preferFactor, 2), 1))
        dailyCosMark.append((random.random() > 0.5 / preferFactor))     # 点赞
        dailyCosMark.append((random.random() > 0.5 / preferFactor))     # 收藏
        dailyCosMark.append(currDate)                                   # 日期
        userData[userId][3][dailyCosId] = dailyCosMark
    return userData, dailyRecordList


'''初始化数据生成'''
def init():
    global startUserId, usersTotalNum, userData,sysData
    for i in range(startUserId, startUserId + usersTotalNum):
        userData = initDataGenerate(i)
        sysData.append(userData)
    print(sysData)
    print("init data generation completed!\n")
# init() # 初始化


'''main'''
if __name__ == '__main__':
    init()
    timeDateForm = initDate
    time.sleep(0.001)
    for day in range(1, 50): # 日期遍历（eg：更新4天的阅览记录）
        currDateForm = timeDateForm - day * datetime.timedelta(days = 1)
        currDate = int(currDateForm.timestamp() * 1000000)
        for i in range(startUserId, startUserId + usersTotalNum): # 用户id遍历
            if i in range(1000, 1040):    # 中二
                setUserImg('zhonger')
                recordList.append(imgDailyGenerate(1, i, currDate)[1])
            elif i in range(1040, 1080):  # 现充
                setUserImg('xianchong')
                recordList.append(imgDailyGenerate(1, i, currDate)[1])
            elif i in range(1080, 1120):  # 肥宅
                setUserImg('feizhai')
                recordList.append(imgDailyGenerate(1, i, currDate)[1])
            elif i in range(1120, 1160):  # 志怪
                setUserImg('zhiguai')
                recordList.append(imgDailyGenerate(1, i, currDate)[1])
            elif i in range(1160, 1200):  # 青春
                setUserImg('qingchun')
                recordList.append(imgDailyGenerate(1, i, currDate)[1])
            # else:                           # 无特定画像
            #     recordList.append(imgDailyGenerate(0, i, currDate)[1])
    print('generate completed!')
    print(recordList)
    # 写入json文件中（多行写入）
    with open("sysData.json", "w", encoding='utf-8') as f:
        json.dump(sysData, f, indent = 2, sort_keys = True, ensure_ascii = False)
    print('write into json completed!')