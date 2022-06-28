#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/27 10:41
@Author: CloudAndMist
@Description:
'''

import json
from dao.userAnimeHistoryDao import getAnimeHistoryByUserId
from dao.userComicHistoryDao import getComicHistoryByUserId
from dao.userNovelHistoryDao import getNovelHistoryByUserId
from dao.userDao import getUserById

abandoneList = []
characterList = ['feizhai', 'qingchun', 'xianchong', 'zhiguai', 'zhonger']

userImageDataDir = {}


def fileOpen(fileName: str):
    global userImageDataDir
    with open(f"../assets/userImageDataList/{fileName}SelectList.json", encoding="utf-8") as file:
        tmp_list = json.load(file)
        # 将selectList中anime, comic, novel, cos四个维度的数据id整合到一个统一的list中
        sum_list = tmp_list[0] + tmp_list[1] + tmp_list[2] + tmp_list[3]
        userImageDataDir[fileName] = sum_list


def analysisWatchRatio(ratio: float):
    if ratio > 0.7:
        return ratio
    elif ratio > 0.4:
        return ratio * 0.75
    return ratio * 0.5


def analysisWeight(id: int):
    count = 0
    for i in characterList:
        if id in userImageDataDir[i]:
            count += 1
    if count == 1:
        return count * 0.2
    return count


def characterAnalysis(character: str):
    totalScore = 0
    for i in userHistoryList:
        if i.historyid in userImageDataDir[character]:
            totalScore += float(i.ratio) / analysisWeight(i.historyid)
    return totalScore


def userAnalysis(uid: int):
    global userHistoryList
    userInfo = getUserById(uid)
    userAnimeHistoryList = getAnimeHistoryByUserId(uid)
    userComicHistoryList = getComicHistoryByUserId(uid)
    userNovelHistoryList = getNovelHistoryByUserId(uid)
    userHistoryList = userAnimeHistoryList + userComicHistoryList + userNovelHistoryList
    if (userAnimeHistoryList is None) or (userComicHistoryList is None) or (userNovelHistoryList is None):
        raise

    for i in characterList:
        fileOpen(i)

    userImageDir = {}
    for i in characterList:
        userImageDir[i] = characterAnalysis(i)

    print("user: ", userInfo.uname)

    return userImageDir


print(userAnalysis(1025))
print(userAnalysis(1045))
print(userAnalysis(1095))
print(userAnalysis(1140))
print(userAnalysis(1180))
