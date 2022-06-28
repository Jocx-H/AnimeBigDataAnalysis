#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :   utils.py
@Time   :   2022/06/23 15:19:31
@Author :   ferry-hhh
@Desc   :   推荐系统的一些参数
'''
import datetime
import numpy as np
import warnings

RATING_PATH = r"G:\GitHub\AnimeBigDataAnalysis\dataGetAndProcess\data_generation\sysDataV2.json"
DATA_PATH = r"G:\GitHub\AnimeBigDataAnalysis\back\assets\simMatrix"

ANIME = 1
COMIC = 2
NOVEL = 3

# 与目标用户兴趣相似的20个用户
SIM_USERS = 20
# 在首页/详情页推荐12部动漫
REC_ITEMS = 12
# 与目标动漫相似的20部其他动漫
SIM_ITEMS = 20
# 当前时间戳（最大时间戳）
# initDate = datetime.datetime.now()
# MAX_TIMESTAMP = int(initDate.timestamp() * 1000000)
MAX_TIMESTAMP = 1656382982995091

def get_time_score(timestamp):
    """
    time decay（时间衰减），即不同时期的行为所占权重不同获取时间权重
    :param timestamp: input timestamp
    :return: time score
    """

    # convert seconds to days
    total_sec = 24 * 60 * 60
    delta = (MAX_TIMESTAMP - timestamp) / total_sec / 100000000
    # delta 越小，得分越高，最高分为1
    return round(1 / (1 + delta), 3)


def perfer_cal(score,collect,up,view_ratio,timestamp):
    """
    综合用户评分、收藏、点赞、观看比例、时间戳得到一个综合评分
    
    param line:数据库中的一行数据
    return:综合评分
    """
    weight = [0.54, 0.30, 0.16]
    if weight == None:
        # 准则重要性矩阵
        criteria = np.array([[1, 2, 3],
                            [1 / 2, 1, 2],
                            [1 / 3, 1 / 2, 1]])
        weight = AHP(criteria).run()
    score2 = collect*weight[0] + up*weight[1] + view_ratio*weight[2]
    res_score = 0
    # 评分是1和2表示用户不喜欢，则收藏等加深了不喜欢程度，时间越新则权重越大
    if score > 0 and score <= 2:
        res_score = (score - score2) * get_time_score(timestamp)
        if res_score < 0:
            res_score = 0
    # 评分是3、4、5表示用户喜欢，则收藏等加深了喜欢程度
    else:
        res_score = (score + score2) * get_time_score(timestamp)
    return res_score


'''
层次分析法计算收藏、点赞、观看比例的影响权重
'''
class AHP:
    def __init__(self, criteria):
        self.RI = (0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49)
        self.criteria = criteria
        self.num_criteria = criteria.shape[0]

    def cal_weights(self, input_matrix):
        input_matrix = np.array(input_matrix)
        n, n1 = input_matrix.shape
        assert n == n1, '不是一个方阵'
        for i in range(n):
            for j in range(n):
                if np.abs(input_matrix[i, j] * input_matrix[j, i] - 1) > 1e-7:
                    raise ValueError('不是反互对称矩阵')

        eigenvalues, eigenvectors = np.linalg.eig(input_matrix)

        max_idx = np.argmax(eigenvalues)
        max_eigen = eigenvalues[max_idx].real
        eigen = eigenvectors[:, max_idx].real
        eigen = eigen / eigen.sum()

        if n > 9:
            CR = None
            warnings.warn('无法判断一致性')
        else:
            CI = (max_eigen - n) / (n - 1)
            CR = CI / self.RI[n]
        return max_eigen, CR, eigen

    def run(self):
        max_eigen, CR, criteria_eigen = self.cal_weights(self.criteria)
        return criteria_eigen


