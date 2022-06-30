#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:42
@Author: Jocx, WILLOSCAR, CloudAndMist
@Description:
  提供给热门推荐API的服务，包括：
      按热度降序排序动漫、小说、漫画和cosplay
'''

import json
import random
import traceback

from operator import itemgetter

from dao import animeDao, comicDao, novelDao, cosplayDao


MATRIX_PATH = r'./assets/simMatrix/{}.json'
MAX_SIM_USER_COUNT = 20
MAX_USER_ITEM_COUNT = 60
RANDOM_COUNT = 12


def __statAnime__(uid: int):
    r"""
    通过用户相似度矩阵和用户物品爱好矩阵推荐动漫
    """
    sim_matrix_path = MATRIX_PATH.format('anime_user_sim')
    user_item_path = MATRIX_PATH.format('anime_user_item')
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(user_item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        anime_dict = animeDao.getAnimeDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    uid = str(uid)
    rank = {}
    watched_items = user_item[uid]
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[:MAX_SIM_USER_COUNT]
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            if item in watched_items: continue
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    recommoned_res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    recommoned_res = random.sample(recommoned_res, RANDOM_COUNT)
    dir_res = {
        "aid": [],
        "title": [],
        "cover": [],
    }
    for k in recommoned_res:
        dir_res["aid"].append(anime_dict[int(k[0])]["aid"])
        dir_res["title"].append(anime_dict[int(k[0])]["title"])
        dir_res["cover"].append(anime_dict[int(k[0])]["cover"])

    return dir_res


def __statNovel__(uid: int):
    r"""
    通过用户相似度矩阵和用户物品爱好矩阵推荐小说
    """
    sim_matrix_path = MATRIX_PATH.format('novel_user_sim')
    user_item_path = MATRIX_PATH.format('novel_user_item')
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(user_item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        novel_dict = novelDao.getNovelDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    uid = str(uid)
    rank = {}
    watched_items = user_item[uid]
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[:MAX_SIM_USER_COUNT]
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            if item in watched_items: continue
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    recommoned_res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    recommoned_res = random.sample(recommoned_res, RANDOM_COUNT)
    dir_res = {
        "nid": [],
        "cover": [],
        "title": [],
    }
    for k in recommoned_res:
        dir_res["nid"].append(novel_dict[int(k[0])]["nid"])
        dir_res["cover"].append(novel_dict[int(k[0])]["cover"])
        dir_res["title"].append(novel_dict[int(k[0])]["title"])

    return dir_res


def __statComic__(uid: int):
    r"""
    通过用户相似度矩阵和用户物品爱好矩阵推荐漫画
    """
    sim_matrix_path = MATRIX_PATH.format('comic_user_sim')
    user_item_path = MATRIX_PATH.format('comic_user_item')
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(user_item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        comic_dict = comicDao.getComicDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    uid = str(uid)
    rank = {}
    watched_items = user_item[uid]
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[:MAX_SIM_USER_COUNT]
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            if item in watched_items: continue
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    recommoned_res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    recommoned_res = random.sample(recommoned_res, RANDOM_COUNT)
    dir_res = {
        "cid": [],
        "cover": [],
        "title": [],
    }
    for k in recommoned_res:
        dir_res["cid"].append(comic_dict[int(k[0])]["cid"])
        dir_res["cover"].append(comic_dict[int(k[0])]["cover"])
        dir_res["title"].append(comic_dict[int(k[0])]["title"])

    return dir_res


def __statCosplay__(uid: int):
    r"""
    通过用户相似度矩阵和用户物品爱好矩阵推荐cosplay
    """
    cosplays = list(cosplayDao.getCosplayDict().items())
    cosplays = random.sample(cosplays, RANDOM_COUNT)
    dir_res = {
        "cosid": [],
        "cover": [],
        "title": [],
        "url": []
    }
    for k in cosplays:
        dir_res["cosid"].append(k[1]["cosid"])
        dir_res["cover"].append(k[1]["cover"])
        dir_res["title"].append(k[1]["title"])
        dir_res["url"].append(k[1]["url"])
    return dir_res


def getAnime(uid: int) -> dict:
    return {'result': __statAnime__(uid)}


def getNovel(uid: int) -> dict:
    return {'result': __statNovel__(uid)}


def getComic(uid: int) -> dict:
    return {'result': __statComic__(uid)}


def getCosplay(uid: int) -> dict:
    return {'result': __statCosplay__(uid)}


# TEST
'''
单元测试：
  getAnime(uid)
  getNovel(uid)
  getComic(uid)
  getCosplay(uid)
'''
if __name__ == '__main__':
    MATRIX_PATH = r'..\assets\simMatrix\{}.json'
    print(getAnime(1000))
    print(getNovel(1000))
    print(getComic(1000))
    print(getCosplay(1000))