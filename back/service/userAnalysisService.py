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

def analysisWatchRatio(ratio: float):
    if ratio > 0.7:
        return ratio
    elif ratio > 0.4:
        return ratio * 0.75
    return ratio * 0.5


def userAnalysis(uid: int):
    userAnimeHistoryList = getAnimeHistoryByUserId(uid)
    userComicHistoryList = getComicHistoryByUserId(uid)
    userNovelHistoryList = getNovelHistoryByUserId(uid)
    if (userAnimeHistoryList is None) or (userComicHistoryList is None) or (userNovelHistoryList is None):
        raise
    userImageDataDir = {}
    with open("../assets/userImageDataList/feizhaiSelectList.json", encoding="utf-8") as file:
        userImageDataDir['feizhai'] = json.load(file)
    print(type(userImageDataDir['feizhai']))


    result = {}

    return result
