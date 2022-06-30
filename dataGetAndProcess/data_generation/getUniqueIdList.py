# -*- coding = utf-8 -*-
# @Time : 2022/6/27 21:27
# @File : getUniqueIdList.py
# @Author : derrick

import json

'''
用于获取只对应一个用户画像的作品
'''

def zhongerUniqueIdList():
    uniqueIdList = []
    with open("selectList/zhongerSelectList.json", encoding ="utf-8") as file:
        zhongerList = json.load(file)
    with open("selectList/xianchongSelectList.json", encoding ="utf-8") as file:
        xianchongList = json.load(file)
    with open("selectList/feizhaiSelectList.json", encoding ="utf-8") as file:
        feizhaiList = json.load(file)
    with open("selectList/zhiguaiSelectList.json", encoding ="utf-8") as file:
        zhiguaiList = json.load(file)
    with open("selectList/qingchunSelectList.json", encoding ="utf-8") as file:
        qingchunList = json.load(file)
    # print(zhongerList)
    # print(xianchongList)
    for i in range(len(zhongerList) - 1):
        workList = []
        for j in range(len(zhongerList[i])):
            if (zhongerList[i][j] not in xianchongList[i]) and (zhongerList[i][j] not in feizhaiList[i]) \
                and (zhongerList[i][j] not in zhiguaiList[i]) and (zhongerList[i][j] not in qingchunList[i]):
                workList.append(zhongerList[i][j])
                # print(zhongerList[i][j])
        uniqueIdList.append(workList)
    # 写入json文件中（多行写入）
    with open("uniqueList/zhongerUniqueIdList.json", "w", encoding='utf-8') as f:
        json.dump(uniqueIdList, f, indent=2, sort_keys=True, ensure_ascii=False)
    return uniqueIdList


def xianchongUniqueIdList():
    uniqueIdList = []
    with open("selectList/zhongerSelectList.json", encoding ="utf-8") as file:
        zhongerList = json.load(file)
    with open("selectList/xianchongSelectList.json", encoding ="utf-8") as file:
        xianchongList = json.load(file)
    with open("selectList/feizhaiSelectList.json", encoding ="utf-8") as file:
        feizhaiList = json.load(file)
    with open("selectList/zhiguaiSelectList.json", encoding ="utf-8") as file:
        zhiguaiList = json.load(file)
    with open("selectList/qingchunSelectList.json", encoding ="utf-8") as file:
        qingchunList = json.load(file)
    for i in range(len(xianchongList) - 1):
        workList = []
        for j in range(len(xianchongList[i])):
            if (xianchongList[i][j] not in zhongerList[i]) and (xianchongList[i][j] not in feizhaiList[i]) \
                and (xianchongList[i][j] not in zhiguaiList[i]) and (xianchongList[i][j] not in qingchunList[i]):
                workList.append(xianchongList[i][j])
                # print(zhongerList[i][j])
        uniqueIdList.append(workList)
    # 写入json文件中（多行写入）
    with open("uniqueList/xianchongUniqueIdList.json", "w", encoding='utf-8') as f:
        json.dump(uniqueIdList, f, indent=2, sort_keys=True, ensure_ascii=False)
    return uniqueIdList


def feizhaiUniqueIdList():
    uniqueIdList = []
    with open("selectList/zhongerSelectList.json", encoding ="utf-8") as file:
        zhongerList = json.load(file)
    with open("selectList/xianchongSelectList.json", encoding ="utf-8") as file:
        xianchongList = json.load(file)
    with open("selectList/feizhaiSelectList.json", encoding ="utf-8") as file:
        feizhaiList = json.load(file)
    with open("selectList/zhiguaiSelectList.json", encoding ="utf-8") as file:
        zhiguaiList = json.load(file)
    with open("selectList/qingchunSelectList.json", encoding ="utf-8") as file:
        qingchunList = json.load(file)
    for i in range(len(feizhaiList) - 1):
        workList = []
        for j in range(len(feizhaiList[i])):
            if (feizhaiList[i][j] not in zhongerList[i]) and (feizhaiList[i][j] not in xianchongList[i]) \
                and (feizhaiList[i][j] not in zhiguaiList[i]) and (feizhaiList[i][j] not in qingchunList[i]):
                workList.append(feizhaiList[i][j])
        uniqueIdList.append(workList)
    # 写入json文件中（多行写入）
    with open("uniqueList/feizhaiUniqueIdList.json", "w", encoding='utf-8') as f:
        json.dump(uniqueIdList, f, indent=2, sort_keys=True, ensure_ascii=False)
    return uniqueIdList

def zhiguaiUniqueIdList():
    uniqueIdList = []
    with open("selectList/zhongerSelectList.json", encoding ="utf-8") as file:
        zhongerList = json.load(file)
    with open("selectList/xianchongSelectList.json", encoding ="utf-8") as file:
        xianchongList = json.load(file)
    with open("selectList/feizhaiSelectList.json", encoding ="utf-8") as file:
        feizhaiList = json.load(file)
    with open("selectList/zhiguaiSelectList.json", encoding ="utf-8") as file:
        zhiguaiList = json.load(file)
    with open("selectList/qingchunSelectList.json", encoding ="utf-8") as file:
        qingchunList = json.load(file)
    for i in range(len(zhiguaiList) - 1):
        workList = []
        for j in range(len(zhiguaiList[i])):
            if (zhiguaiList[i][j] not in zhongerList[i]) and (zhiguaiList[i][j] not in xianchongList[i]) \
                and (zhiguaiList[i][j] not in feizhaiList[i]) and (zhiguaiList[i][j] not in qingchunList[i]):
                workList.append(zhiguaiList[i][j])
        uniqueIdList.append(workList)
    # 写入json文件中（多行写入）
    with open("uniqueList/zhiguaiUniqueIdList.json", "w", encoding='utf-8') as f:
        json.dump(uniqueIdList, f, indent=2, sort_keys=True, ensure_ascii=False)
    return uniqueIdList

def qingchunUniqueIdList():
    uniqueIdList = []
    with open("selectList/zhongerSelectList.json", encoding ="utf-8") as file:
        zhongerList = json.load(file)
    with open("selectList/xianchongSelectList.json", encoding ="utf-8") as file:
        xianchongList = json.load(file)
    with open("selectList/feizhaiSelectList.json", encoding ="utf-8") as file:
        feizhaiList = json.load(file)
    with open("selectList/zhiguaiSelectList.json", encoding ="utf-8") as file:
        zhiguaiList = json.load(file)
    with open("selectList/qingchunSelectList.json", encoding ="utf-8") as file:
        qingchunList = json.load(file)
    for i in range(len(qingchunList) - 1):
        workList = []
        for j in range(len(qingchunList[i])):
            if (qingchunList[i][j] not in zhongerList[i]) and (qingchunList[i][j] not in xianchongList[i]) \
                and (qingchunList[i][j] not in feizhaiList[i]) and (qingchunList[i][j] not in zhiguaiList[i]):
                workList.append(qingchunList[i][j])
        uniqueIdList.append(workList)
    # 写入json文件中（多行写入）
    with open("uniqueList/qingchunUniqueIdList.json", "w", encoding='utf-8') as f:
        json.dump(uniqueIdList, f, indent=2, sort_keys=True, ensure_ascii=False)
    return uniqueIdList


if __name__ == "__main__":
    print(zhongerUniqueIdList())
    print(xianchongUniqueIdList())
    print(feizhaiUniqueIdList())
    print(zhiguaiUniqueIdList())
    print(qingchunUniqueIdList())