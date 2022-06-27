#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :   ItemCF.py
@Time   :   2022/06/23 15:17:41
@Author :   ferry-hhh
@Desc   :   基于物品的推荐，放在详情页
'''

from math import sqrt
from operator import itemgetter
import json
import os

from utils import *

class ItemBasedCF():
    def __init__(self, kind, filename):
        """
        初始化参数
        """
        # 用户-动漫矩阵
        # {u1:{i1:9,i2:7,i3:8},
        #  u2:{i2:9,i4:8,i5:10}}
        self.user_item = {}
        # 动漫相似度矩阵
        # {i1:{i1:0,i2:0.8,i3:0.2},
        #  i2:{i1:0.8,i2:0,i3:0.1},
        #  i3:{i1:0.2,i2:0.1,i3:0}}
        self.item_sim_matrix = {}
        # 动漫热度列表，值是喜欢该动漫的人数
        # {i1:4,
        #  i2:5,
        #  i3:2}
        self.item_popular = {}
        self.item_count = 0
        self.filename = filename
        self.kind = ANIME if kind == None else kind
        self.user_item_name = "anime_user_item.json"
        self.item_sim_name = "anime_item_sim.json"
        if self.kind == ANIME:
            self.item_sim_name = "anime_item_sim.json"
            self.user_item_name = "anime_user_item.json"
        elif self.kind == COMIC:
            self.item_sim_name = "comic_item_sim.json"
            self.user_item_name = "comic_user_item.json"
        elif self.kind == NOVEL:
            self.item_sim_name = "novel_item_sim.json"
            self.user_item_name = "novel_user_item.json"

        # 首先检查是否已经预处理完成了用户-物品矩阵与用户相似度矩阵
        try:
            with open(os.path.join(DATA_PATH, self.user_item_name), "r") as f1:
                self.user_item = json.load(f1)
            with open(os.path.join(DATA_PATH, self.item_sim_name), "r") as f2:
                self.item_sim_matrix = json.load(f2)
        except FileNotFoundError:
            self.get_dataset()
            self.calc_item_sim()
            self.save()

    def get_dataset(self):
        """
        读取数据集构建`用户-动漫`矩阵
        
        param filename : 数据集文件路径
        """
        result = {}
        with open(self.filename, 'r') as f:
            result = json.load(f)
            for i in range(len(result)):
                user = result[i]
                user_id = list(user.keys())[0]   # 用户id
                datas = list(user.values())[0]   # 数据
                item_dict = {}
                if self.kind == ANIME:
                    item_dict = datas[0].items()
                elif self.kind == COMIC:
                    item_dict = datas[1].items()
                elif self.kind == NOVEL:
                    item_dict = datas[2].items()
                for item in item_dict:
                    score = item[1][0]
                    collect = int(item[1][3])
                    up = int(item[1][2])
                    view_ratio = item[1][1]
                    timestamp = item[1][4]
                    prefer_score = perfer_cal(score,collect,up,view_ratio,timestamp)
                    self.user_item.setdefault(user_id, {})
                    self.user_item[user_id][item[0]] = prefer_score
        print('='*10, '加载 %s 成功!' % self.filename, '='*10)

    def calc_item_sim(self):
        """
        计算动漫之间的相似度
        计算方法：余弦相似度
        return:动漫相似度矩阵
        """
        for user, items in self.user_item.items():
            for item in items:
                if not self.item_popular.__contains__(item):
                    self.item_popular[item] = 0
                self.item_popular[item] += 1
        print('='*10, '动漫热度列表构建完毕', '='*10)
        self.item_count = len(self.item_popular)

        # 共现矩阵，C[i][j]代表的含义是同时喜欢物品i和物品j的用户数量
        # {i1:{i1:0,i2:1,i3:3},
        #  i2:{i1:1,i2:0,i3:2},
        #  i3:{i1:3,i2:2,i3:0}}
        for user, items in self.user_item.items():
            for a1 in items:
                for a2 in items:
                    if a1 == a2:continue
                self.item_sim_matrix.setdefault(a1, {})
                self.item_sim_matrix[a1].setdefault(a2, 0)
                self.item_sim_matrix[a1][a2] += 1
        print('='*10, '动漫共现矩阵构建完毕', '='*10)

        # 计算动漫之间的相似性
        for a1, related_items in self.item_sim_matrix.items():
            for a2, count in related_items.items():
                if self.item_popular[a1] == 0 or self.item_popular[a2] == 0:
                    self.item_sim_matrix[a1][a2] = 0
                else:
                    self.item_sim_matrix[a1][a2] = count / sqrt(self.item_popular[a1]*self.item_popular[a2])
        print('='*10, '动漫相似度矩阵构建完毕', '='*10)

    def item_rec(self, user, curr_item="c"):
        """
        针对目标用户u以及当前浏览物品c，找到与u的历史记录最相似的20部动漫，产生12个推荐（与c相似的动漫权重大一点）
        
        param user:目标用户u
        param curr_item:当前浏览物品c
        return: 12部推荐的动漫
        """
        rank = {}
        watched_items = self.user_item[user]
        # print(watched_items)
        curr_item_w = 1
        for item, rating in watched_items.items():
            # 与历史记录动漫最相似的20部动漫
            sorted_items = sorted(self.item_sim_matrix[item].items(), key=itemgetter(1), reverse=True)[:SIM_ITEMS]
            # TODO 完善计算用户兴趣度的方法
            # related_item是相关动漫，w是当前动漫与相关动漫的相似度，rating是目标用户对当前动漫的评分
            if item == curr_item:
                curr_item_w = 2
            else:
                curr_item_w = 1
            for related_item, w in sorted_items:
                if related_item in watched_items:continue
                rank.setdefault(related_item, 0)
                rank[related_item] += w * float(rating) * curr_item_w
        res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:REC_ITEMS]
        print('推荐12部动漫：', res)
        return res

    def save(self):
        with open(os.path.join(DATA_PATH, self.item_sim_name), "w") as f:
            f.write(json.dumps(self.item_sim_matrix, ensure_ascii=False, indent=4, separators=(',', ':')))
        with open(os.path.join(DATA_PATH, self.user_item_name), "w") as f:
            f.write(json.dumps(self.user_item, ensure_ascii=False, indent=4, separators=(',', ':')))
        print('='*10, '用户-物品矩阵与物品相似度矩阵保存成功', '='*10)

if __name__ == "__main__":
    userCF = ItemBasedCF(NOVEL, RATING_PATH)
    userCF.item_rec("1000", "177")
