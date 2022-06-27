#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: analysisT.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 27, 2022
# ---
import json

import numpy as np
import pymysql
from dao.utils import database
import numpy

sys_json_path = "../../dataGetAndProcess/data_generation/sysData.json"
with open(sys_json_path, encoding="utf-8") as file:
    file_json = json.load(file)
zhonegr = []
qingchun = []
xianchong = []
zhiguai = []
feizhai = []


def singleTest(userId):
    for item in file_json:
        if list(item.keys())[0] == str(userId):
            return item


def getList(file_path):
    with open(file_path, encoding="utf-8") as f:
        json_list = json.load(f)
    return json_list


def analysisWatchRatio(ratio: float):
    if ratio > 0.7:
        return ratio
    elif ratio > 0.4:
        return ratio * 0.75
    return ratio * 0.5


if __name__ == '__main__':
    id = 1001
    rec = singleTest(id)
    rec = rec[str(id)]
    root_path = "../assets/userImageDataList/"
    zhonger_file_path = root_path + "zhongerSelectList.json"
    qingchun_file_path = root_path + "qingchunSelectList.json"
    xianchong_file_path = root_path + "xianchongSelectList.json"
    zhiguai_file_path = root_path + "zhiguaiSelectList.json"
    feizhai_file_path = root_path + "feizhaiSelectList.json"
    zhonegr = getList(zhonger_file_path)[0]
    qingchun = getList(qingchun_file_path)[0]
    xianchong = getList(xianchong_file_path)[0]
    zhiguai = getList(zhiguai_file_path)[0]
    feizhai = getList(feizhai_file_path)[0]
    scoreList = []
    # key=id value=[3,0.58,true,true,timestamp]
    zhongerScore = 0
    qingchunScore = 0
    xianchongScore = 0
    zhiguaiScore = 0
    feizhaiScore = 0
    for rf in rec:
        for keyID, valueList in rf.items():
            ID = int(keyID)
            value = list(valueList)
            value[1] = float(value[1])
            if ID in zhonegr:
                zhongerScore += analysisWatchRatio(value[1])
            if ID in qingchun:
                qingchunScore += analysisWatchRatio(value[1])
            if ID in xianchong:
                xianchongScore += analysisWatchRatio(value[1])
            if ID in zhiguai:
                zhiguaiScore += analysisWatchRatio(value[1])
            if ID in feizhai:
                feizhaiScore += analysisWatchRatio(value[1])
    scoreList = [zhongerScore, qingchunScore, xianchongScore, zhiguaiScore, feizhaiScore]
    attrList = ["zhonger", "qingchun", "xianchong", "zhiguai", "feizhai"]
    index = np.argmax(scoreList)
    identification = attrList[index]
