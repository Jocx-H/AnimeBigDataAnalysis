# -*- coding: gbk -*-
import random
import time
from typing import MappingView
import json

'''
userHistoryGeneration.py
�������ܣ�
1.�����û���ʷ��
2.ÿ��������¼��
'''

# ������Ʒ����
animeTotalNum = 3531    # ��������
comicTotalNum = 20931   # ��������
novelTotalNum = 9841    # С˵����
cosTotalNum = 200       # cosplay ����
# ÿ�� �� ����������������С˵�ĸ���
animeDailyRate = 0.3
comicDailyRate = 0.3
novelDailyRate = 0.3
cosDailyRate = 0.5
# ȫ�ֱ�����Ϣ����
usersTotalNum = 3    # �û�����
startUserId = 10000     # ��ʼ�û�ID
userData = []           # �����û������б�
sysData = []            # ϵͳ�û�������: [userData[], userData[], ...]

'''���ɵ����û���ʷ������������'''
def generateHistory(userId: int):
    # userData˵��:
    # list����: [userId, {12:[3, 0.85, 1, 0], 45: [4, 0.40, 0, 1], ...}, {12:[3, 0.85, 0, 0], 45: [4, 0.40, 1, 1], ...}, ...]
    # ��һ�����û�ID,�ڶ��������ġ�����ֱ��Ƕ�����������С˵��cosplay��¼���ֵ����ͣ�
    # ��Ʒ����: ����5��,��ͷ�1��,0�ֱ�ʾ�ۿ���δ����
    # mark�б��д��Ī�û���Ʒ�Ĺۿ���Ϣ��������(int)���ۿ�ʱ��ռ��ʱ��ռ��(float)������(bool)���ղ�(bool)���ɣ�[score, timePercentage, like, collect]
    userData = []
    userData.append(userId)
    # ���� ��Ʒ���1��ͷ
    animeNum = int(3 + 20*(random.random()))            # ��������û��ۿ�������
    animeDic = {}  # �û��ۿ�����Ϣ�б�
    for i in range(animeNum):
        animeIdList = ['1', str(int(animeTotalNum * random.random()))]
        animeId = int(''.join(animeIdList))             # ��Ʒ���
        animeMark = []                                  # [score, timePercentage]
        animeMark.append(int(random.random() * 6))      # �û�����
        animeMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        animeMark.append((random.random() > 0.5))       # ����
        animeMark.append((random.random() > 0.5))       # �ղ�
        animeDic[animeId] = animeMark
    userData.append(animeDic)
    # ���� ��Ʒ���2��ͷ
    comicNum = int(3 + 20*(random.random()))
    comicDic = {}
    for i in range(comicNum):
        comicIdList = ['2', str(int(comicTotalNum * random.random()))]
        comicId = int(''.join(comicIdList))             # ��Ʒ���
        comicMark = []
        comicMark.append(int(random.random() * 6))      # �û�����
        comicMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        comicMark.append((random.random() > 0.5))       # ����
        comicMark.append((random.random() > 0.5))       # �ղ�
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # С˵ ��Ʒ���3��ͷ
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelIdList = ['3', str(int(novelTotalNum * random.random()))]
        novelId = int(''.join(novelIdList))             # ��Ʒ���
        novelMark = []
        novelMark.append(int(random.random() * 6))      # �û�����
        novelMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        novelMark.append((random.random() > 0.5))       # ����
        novelMark.append((random.random() > 0.5))       # �ղ�
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    # cosplay ��Ʒ���4��ͷ
    cosNum = int(3 + 20 * (random.random()))
    cosDic = {}
    for i in range(cosNum):
        cosIdList = ['3', str(int(cosTotalNum * random.random()))]
        cosId = int(''.join(cosIdList))  # ��Ʒ���
        cosMark = []
        cosMark.append(int(random.random() * 6))        # �û�����
        cosMark.append(round(random.random(), 2))       # �û��ۿ�ʱ���ٷֱ�
        cosMark.append((random.random() > 0.5))         # ����
        cosMark.append((random.random() > 0.5))         # �ղ�
        cosDic[cosId] = cosMark
    userData.append(cosDic)
    return userData

'''����ÿ��������¼����ӣ�'''
def generateDailyBrowsing(userData: list):
    dailyRecordList = []  # �û�record.py�е�recordList����¼�û�ÿ��ۿ��ĸ���������Ʒ����Ϣ
    # ����
    dailyAnimeNum = int(random.random() * 5) if random.random() > animeDailyRate else 0
    for i in range(dailyAnimeNum):
        dailyRecordList.append(1)
        dailyAnimeIdList = ['1', str(int(animeTotalNum * random.random()))]
        dailyAnimeId = int(''.join(dailyAnimeIdList))
        dailyAnimeMark = []
        dailyAnimeMark.append(int(random.random() * 6))
        dailyAnimeMark.append(round(random.random(), 2))
        dailyAnimeMark.append((random.random() > 0.5))  # ����
        dailyAnimeMark.append((random.random() > 0.5))  # �ղ�
        userData[1][dailyAnimeId] = dailyAnimeMark
    # ����
    time.sleep(0.01)
    dailyComicNum = int(random.random() * 5) if random.random() > comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyRecordList.append(2)
        dailyComicIdList = ['2', str(int(comicTotalNum * random.random()))]
        dailyComicId = int(''.join(dailyComicIdList))
        dailyComicMark = []
        dailyComicMark.append(int(random.random() * 6))
        dailyComicMark.append(round(random.random(), 2))
        dailyComicMark.append((random.random() > 0.5))  # ����
        dailyComicMark.append((random.random() > 0.5))  # �ղ�
        userData[2][dailyComicId] = dailyComicMark
    # С˵
    time.sleep(0.01)
    dailyNovelNum = int(random.random() * 5) if random.random() > novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyRecordList.append(3)
        dailyNovelIdList = ['3', str(int(novelTotalNum * random.random()))]
        dailyNovelId = int(''.join(dailyNovelIdList))
        dailyNovelMark = []
        dailyNovelMark.append(int(random.random() * 6))
        dailyNovelMark.append(round(random.random(), 2))
        dailyNovelMark.append((random.random() > 0.5))  # ����
        dailyNovelMark.append((random.random() > 0.5))  # �ղ�
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
        dailyCosMark.append((random.random() > 0.5))  # ����
        dailyCosMark.append((random.random() > 0.5))  # �ղ�
        userData[4][dailyCosId] = dailyCosMark
    return userData, dailyRecordList


# ���Դ���
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
#     # json.dump(dict_, f)  # дΪһ��
#     json.dump(sysData, f, indent = 2, sort_keys = True, ensure_ascii = False)  # дΪ����