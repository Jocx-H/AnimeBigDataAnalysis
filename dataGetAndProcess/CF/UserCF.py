#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :   UserCF.py
@Time   :   2022/06/23 15:17:16
@Author :   ferry-hhh
@Desc   :   基于用户的推荐，放在首页
'''

from math import sqrt
from operator import itemgetter
import json
import os

from utils import *

class UserBasedCF():
    def __init__(self, kind, filename):
        """
        初始化参数
        """
        # 用户-动漫矩阵
        # {u1:{i1:9,i2:7,i3:8},
        #  u2:{i2:9,i4:8,i5:10}}
        self.user_item = {}
        # 用户相似度矩阵
        # {u1:{u1:0,u2:0.8,u3:0.2},
        #  u2:{u1:0.8,u2:0,u3:0.1},
        #  u3:{u1:0.2,u2:0.1,u3:0}}
        self.user_sim_matrix = {}
        # 动漫-用户倒排表，为了方便计算喜欢同一部动漫的用户个数
        # {i1:<u1,u2>,
        #  i2:<u2,u3}
        self.item_user = {}
        self.item_count = 0
        self.filename = filename
        self.kind = ANIME if kind == None else kind
        self.user_item_name = "anime_user_item.json"
        self.user_sim_name = "anime_user_sim.json"
        if self.kind == ANIME:
            self.user_sim_name = "anime_user_sim.json"
            self.user_item_name = "anime_user_item.json"
        elif self.kind == COMIC:
            self.user_sim_name = "comic_user_sim.json"
            self.user_item_name = "comic_user_item.json"
        elif self.kind == NOVEL:
            self.user_sim_name = "novel_user_sim.json"
            self.user_item_name = "novel_user_item.json"

        # 首先检查是否已经预处理完成了用户-物品矩阵与用户相似度矩阵
        try:
            with open(os.path.join(DATA_PATH, self.user_item_name), "r") as f1:
                self.user_item = json.load(f1)
            with open(os.path.join(DATA_PATH, self.user_sim_name), "r") as f2:
                self.user_sim_matrix = json.load(f2)
        except FileNotFoundError:
            self.get_dataset()
            self.calc_user_sim()
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

    def calc_user_sim(self):
        """
        计算用户之间的相似度
        计算方法：余弦相似度
        return:用户相似度矩阵
        """
        
        for user, items in self.user_item.items():
            for item in items:
                # 如果该动漫还不在矩阵里，那么为之建立一个set加入进来
                if not self.item_user.__contains__(item):
                    self.item_user[item] = set()
                self.item_user[item].add(user)
        print('='*10, '动漫-用户矩阵构建完毕', '='*10)

        # 统计有多少部动漫
        self.item_count = len(self.item_user)
        
        # 建立用户喜爱物品交集矩阵（对称矩阵）
        # {u1:{u1:0,u2:3,u3:1},
        #  u2:{u1:3,u2:0,u3:2},
        #  u3:{u1:1,u2:2,u3:0}}
        for item, users in self.item_user.items():
            for u in users:
                for v in users:
                    if u == v: continue
                    self.user_sim_matrix.setdefault(u, {})
                    self.user_sim_matrix[u].setdefault(v, 0)
                    self.user_sim_matrix[u][v] += 1
        print('='*10, '用户喜爱物品交集矩阵构建完毕', '='*10)

        # 计算用户相似度
        # TODO 添加惩罚因子改进算法
        for u, related_users in self.user_sim_matrix.items():
            for v, count in related_users.items():
                self.user_sim_matrix[u][v] = count / sqrt(len(self.user_item[u])*len(self.user_item[v]))
        print('='*10, '用户相似度矩阵计算完毕', '='*10)

    def user_rec(self, user):
        """
        针对目标用户u，找到与之最相似的20个用户，产生12个推荐
        
        param user:目标用户u
        return: 12部推荐的动漫
        """
        rank = {}
        watched_items = self.user_item[user]
        # 与目标用户最相似的20个用户
        sorted_users = sorted(self.user_sim_matrix[user].items(), key=itemgetter(1),reverse=True)[0:SIM_USERS]
        # v是相似用户，Wuv是u与v的相似度
        for v, Wuv in sorted_users:
            for item in self.user_item[v]:
                if item in watched_items:continue
                rank.setdefault(item, 0)
                rank[item] += Wuv * float(self.user_item[v][item])
        res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:REC_ITEMS]
        print('推荐12部动漫：', res)
        return res

    def save(self):
        with open(os.path.join(DATA_PATH, self.user_sim_name), "w") as f:
            f.write(json.dumps(self.user_sim_matrix, ensure_ascii=False, indent=4, separators=(',', ':')))
        with open(os.path.join(DATA_PATH, self.user_item_name), "w") as f:
            f.write(json.dumps(self.user_item, ensure_ascii=False, indent=4, separators=(',', ':')))
        print('='*10, '用户-物品矩阵与用户相似度矩阵保存成功', '='*10)


if __name__ == "__main__":
    userCF = UserBasedCF(NOVEL, RATING_PATH)
    userCF.user_rec("1000")
