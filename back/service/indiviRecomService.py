#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:42
@Author: Jocx
@Description:
  提供给个性化推荐API的服务，包括：
      按用户喜好程度降序排序动漫、小说、漫画
'''

import json
import random
import traceback

from operator import itemgetter

from dao import animeDao, comicDao, novelDao


MATRIX_PATH = r'./assets/simMatrix/{}.json'
MAX_SIM_USER_COUNT = 20
MAX_USER_ITEM_COUNT = 60
RANDOM_COUNT = 12


def __computeAnime__(uid: int, sim_matrix_path: str):
    r"""
    根据推荐算法计算出用户喜爱的动漫
    """
    item_path = MATRIX_PATH.format('anime_user_item')
    uid = str(uid)
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        data_dicts = animeDao.getAnimeDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[0:MAX_SIM_USER_COUNT]
    rank = {}
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    res = random.sample(res, RANDOM_COUNT)
    dir_res = {
        "aid": [],
        "title": [],
        "index_show": [],
        "is_finished": [],
        "video_link": [],
        "cover": [],
        "pub_real_time": [],
        "renewal_time": [],
        "favorites": [],
        "coins": [],
        "views": [],
        "danmakus": [],
        "depth": [],
        "media_tags": [],
        "score": [],
        "cm_count": []
    }
    for k in res:
        dir_res["aid"].append(data_dicts[int(k[0])]["aid"])
        dir_res["title"].append(data_dicts[int(k[0])]["title"])
        dir_res["index_show"].append(data_dicts[int(k[0])]["index_show"])
        dir_res["is_finished"].append(data_dicts[int(k[0])]["is_finished"])
        dir_res["video_link"].append(data_dicts[int(k[0])]["video_link"])
        dir_res["cover"].append(data_dicts[int(k[0])]["cover"])
        dir_res["pub_real_time"].append(data_dicts[int(k[0])]["pub_real_time"])
        dir_res["renewal_time"].append(data_dicts[int(k[0])]["renewal_time"])
        dir_res["favorites"].append(data_dicts[int(k[0])]["favorites"])
        dir_res["coins"].append(data_dicts[int(k[0])]["coins"])
        dir_res["views"].append(data_dicts[int(k[0])]["views"])
        dir_res["danmakus"].append(data_dicts[int(k[0])]["danmakus"])
        dir_res["depth"].append(data_dicts[int(k[0])]["depth"])
        dir_res["media_tags"].append(data_dicts[int(k[0])]["media_tags"])
        dir_res["score"].append(data_dicts[int(k[0])]["score"])
        dir_res["cm_count"].append(data_dicts[int(k[0])]["cm_count"])

    return dir_res


def __computeNovel__(uid: int, sim_matrix_path: str):
    r"""
    根据推荐算法计算出用户喜爱的小说
    """
    item_path = MATRIX_PATH.format('novel_user_item')
    uid = str(uid)
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        data_dicts = novelDao.getNovelDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[0:MAX_SIM_USER_COUNT]
    rank = {}
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    res = random.sample(res, RANDOM_COUNT)
    dir_res = {
        "nid": [],
        "url": [],
        "cover": [],
        "title": [],
        "author": [],
        "score": [],
        "type": [],
        "depth": [],
        "state": [],
        "click_cnt": [],
        "update_time": [],
        "introduce": []
    }
    for k in res:
        dir_res["nid"].append(data_dicts[int(k[0])]["nid"])
        dir_res["url"].append(data_dicts[int(k[0])]["url"])
        dir_res["cover"].append(data_dicts[int(k[0])]["cover"])
        dir_res["title"].append(data_dicts[int(k[0])]["title"])
        dir_res["author"].append(data_dicts[int(k[0])]["author"])
        dir_res["score"].append(data_dicts[int(k[0])]["score"])
        dir_res["type"].append(data_dicts[int(k[0])]["type"])
        dir_res["depth"].append(data_dicts[int(k[0])]["depth"])
        dir_res["state"].append(data_dicts[int(k[0])]["state"])
        dir_res["click_cnt"].append(data_dicts[int(k[0])]["click_cnt"])
        dir_res["update_time"].append(data_dicts[int(k[0])]["update_time"])
        dir_res["introduce"].append(data_dicts[int(k[0])]["introduce"])

    return dir_res


def __computeComic__(uid: int, sim_matrix_path: str):
    r"""
    根据推荐算法计算出用户喜爱的漫画
    """
    item_path = MATRIX_PATH.format('comic_user_item')
    uid = str(uid)
    try:
        with open(sim_matrix_path, 'r', encoding='utf-8') as R:
            sim_matrix = json.load(R)
        with open(item_path, 'r', encoding='utf-8') as R2:
            user_item = json.load(R2)
        data_dicts = comicDao.getComicDict()
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    sorted_users = sorted(sim_matrix[uid].items(), key=itemgetter(1), reverse=True)[0:MAX_SIM_USER_COUNT]
    rank = {}
    for v, Wuv in sorted_users:
        for item in user_item[v]:
            rank.setdefault(item, 0)
            rank[item] += Wuv * float(user_item[v][item])
    res = sorted(rank.items(), key=itemgetter(1), reverse=True)[:MAX_USER_ITEM_COUNT]
    res = random.sample(res, RANDOM_COUNT)
    dir_res = {
        "cid": [],
        "url": [],
        "cover": [],
        "title": [],
        "last_short_title": [],
        "author": [],
        "type": [],
        "state": []
    }
    for k in res:
        dir_res["cid"].append(data_dicts[int(k[0])]["cid"])
        dir_res["url"].append(data_dicts[int(k[0])]["url"])
        dir_res["cover"].append(data_dicts[int(k[0])]["cover"])
        dir_res["title"].append(data_dicts[int(k[0])]["title"])
        dir_res["last_short_title"].append(data_dicts[int(k[0])]["last_short_title"])
        dir_res["author"].append(data_dicts[int(k[0])]["author"])
        dir_res["type"].append(data_dicts[int(k[0])]["type"])
        dir_res["state"].append(data_dicts[int(k[0])]["state"])

    return dir_res


def getAnimeAndNovel(uid: int) -> dict:
    sim_path = MATRIX_PATH.format('anime_user_sim')
    sim_path2 = MATRIX_PATH.format('novel_user_sim')
    return {'result': {'anime': __computeAnime__(uid, sim_path),
                       'novel': __computeNovel__(uid, sim_path2)}}


def getNovelAndComic(uid: int) -> dict:
    sim_path = MATRIX_PATH.format('novel_user_sim')
    sim_path2 = MATRIX_PATH.format('comic_user_sim')
    return {'result': {'novel': __computeAnime__(uid, sim_path),
                       'comic': __computeNovel__(uid, sim_path2)}}


def getAnimeAndComic(uid: int):
    sim_path = MATRIX_PATH.format('anime_user_sim')
    sim_path2 = MATRIX_PATH.format('comic_user_sim')
    return {'result': {'anime': __computeAnime__(uid, sim_path),
                       'comic': __computeNovel__(uid, sim_path2)}}


# TEST
'''
单元测试：
  getAnimeAndNovel(uid)
  getAnimeAndComic(uid)
  getNovelAndComic(uid)
'''
if __name__  == '__main__':
    MATRIX_PATH = r'../assets/simMatrix/{}.json'
    print(getAnimeAndNovel(1001))
    print(getAnimeAndComic(1001))
    print(getNovelAndComic(1001))