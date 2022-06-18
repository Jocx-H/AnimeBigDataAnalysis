# -*- coding: gbk -*-
import random
import time
from typing import MappingView

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
# ÿ������������������С˵�ĸ���
animeDailyRate = 0.5
comicDailyRate = 0.7
novelDailyRate = 0.7
# ȫ�ֱ�����Ϣ����
usersTotalNum = 3    # �û�����
startUserId = 10000     # ��ʼ�û�ID
userData = []           # �����û������б�
sysData = []            # ϵͳ�û�������: [userData[], userData[], ...]

'''���ɵ����û���ʷ������������'''
def generateHistory(userId: int):
    # userData˵��:
    # list����: [userId, {12:[3, 0.85], 45: [4, 0.40], ...}, {12:[3, 0.85], 45: [4, 0.40], ...}, ...]
    # ��һ�����û�ID,�ڶ�����������ֱ��Ƕ�����������С˵��¼���ֵ����ͣ�
    # ��Ʒ����: ����5��,��ͷ�1��,0�ֱ�ʾ�ۿ���δ����
    # mark�б��д��Ī�û���Ʒ�Ĺۿ���Ϣ�������ֺ͹ۿ�ʱ��ռ��ʱ��ռ�ȹ��ɣ�[score, timePercentage]
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
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # С˵ ��Ʒ���3��ͷ
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelIdList = ['3', str(int(novelTotalNum * random.random()))]
        novelId = int(''.join(comicIdList))             # ��Ʒ���
        novelMark = []
        novelMark.append(int(random.random() * 6))      # �û�����
        novelMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    return userData

'''����ÿ��������¼����ӣ�'''
def generateDailyBrowsing(userData: list):
    # ����
    dailyAnimeNum = int(random.random() * 5) if random.random() > animeDailyRate else 0
    for i in range(dailyAnimeNum):
        dailyAnimeIdList = ['1', str(int(animeTotalNum * random.random()))]
        dailyAnimeId = int(''.join(dailyAnimeIdList))
        dailyAnimeMark = []
        dailyAnimeMark.append(int(random.random() * 6))
        dailyAnimeMark.append(round(random.random(), 2))
        userData[1][dailyAnimeId] = dailyAnimeMark
    # ����
    dailyComicNum = int(random.random() * 5) if random.random() > comicDailyRate else 0
    for i in range(dailyComicNum):
        dailyComicIdList = ['2', str(int(comicTotalNum * random.random()))]
        dailyComicId = int(''.join(dailyComicIdList))
        dailyComicMark = []
        dailyComicMark.append(int(random.random() * 6))
        dailyComicMark.append(round(random.random(), 2))
        userData[2][dailyComicId] = dailyComicMark
    # С˵
    dailyNovelNum = int(random.random() * 5) if random.random() > novelDailyRate else 0
    for i in range(dailyNovelNum):
        dailyNovelIdList = ['3', str(int(novelTotalNum * random.random()))]
        dailyNovelId = int(''.join(dailyNovelIdList))
        dailyNovelMark = []
        dailyNovelMark.append(int(random.random() * 6))
        dailyNovelMark.append(round(random.random(), 2))
        userData[3][dailyNovelId] = dailyNovelMark
    return userData


# ���Դ���
for i in range(startUserId, startUserId + usersTotalNum):
    userData = generateHistory(i)
    sysData.append(userData)

print(sysData)
print("\n")

time.sleep(3)

for item in sysData:
    generateDailyBrowsing(item)
print(sysData)