# -*- coding: gbk -*-
import random
from typing import MappingView


def generateHistory(userId: int):
    '''
    userData˵��:
    list����: [userId, {12:[3, 0.85], 45: [4, 0.40], ...}, {12:[3, 0.85], 45: [4, 0.40], ...}, ...]
    ��һ�����û�ID,�ڶ�����������ֱ��Ƕ�����������С˵��¼���ֵ����ͣ�
    ��Ʒ����: ����5��,��ͷ�1��,0�ֱ�ʾ�ۿ���δ����
    '''
    # data�д���û����ݣ���һ�����û�ID���ڶ�����������ֱ��Ƕ�����������С˵��¼���ֵ����ͣ�
    userData = []
    userData.append(userId)
    animeTotalNum = 3531    # ��������
    comicTotalNum = 20931   # ��������
    novelTotalNum = 9841    # С˵����
    # ����
    animeNum = int(3 + 20*(random.random()))            # ��������û��ۿ�������
    animeDic = {}  # �û��ۿ�����Ϣ�б�
    for i in range(animeNum):
        animeId = int(animeTotalNum * random.random())  # ��Ʒ���
        animeMark = []  # [score, timePercentage]
        animeMark.append(int(random.random() * 6))      # �û�����
        animeMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        animeDic[animeId] = animeMark
    userData.append(animeDic)
    # ����
    comicNum = int(3 + 20*(random.random()))
    comicDic = {}
    for i in range(comicNum):
        comicId = int(comicTotalNum * random.random())
        comicMark = []
        comicMark.append(int(random.random() * 6))      # �û�����
        comicMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        comicDic[comicId] = comicMark
    userData.append(comicDic)
    # С˵
    novelNum = int(3 + 20*(random.random()))
    novelDic = {}
    for i in range(novelNum):
        novelId = int(novelTotalNum * random.random())
        novelMark = []
        novelMark.append(int(random.random() * 6))      # �û�����
        novelMark.append(round(random.random(), 2))     # �û��ۿ�ʱ���ٷֱ�
        novelDic[novelId] = novelMark
    userData.append(novelDic)
    return userData

# ��ʷ��¼����
usersTotalNum = 1000       # �û�����
startUserId = 10000     # ��ʼ�û�ID
sysData = []   # ϵͳ�û�������: [userData[], userData[], ...]
for i in range(startUserId, startUserId + usersTotalNum):
    userData = generateHistory(i)
    sysData.append(userData)

print(sysData)
