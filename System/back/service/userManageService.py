#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:43
@Author: Jocx,WILLOSCAR
@Description:
    提供给用户管理API的服务，包括：
        对用户的登录信息进行验证
'''

from fastapi import HTTPException
from hashlib import md5
from dao.userAnimeHistoryDao import getAnimeHistoryByUserId
from dao.userComicHistoryDao import getComicHistoryByUserId
from dao.userNovelHistoryDao import getNovelHistoryByUserId
from dao.userDao import getUserById
from dao.animeDao import getAnimeById
from dao.comicDao import getComicById
from dao.novelDao import getNovelById


def __hashPassword__(password: str):
    r"""
    hd5加密密码
    """
    usrHash = md5()
    usrHash.update(password.encode(encoding='utf-8'))
    return usrHash.hexdigest()


def usrLogin(uid: int, password: str) -> dict:
    r"""
    检查用户账号(uid)和密码是否与数据库中账号密码匹配
    """
    if uid < 1000 or len(password) > 50:
        raise HTTPException(status_code=400, detail="无效的用户名或密码")
    usr = getUserById(uid)
    if usr is None:
        raise HTTPException(status_code=400, detail="查无此人")
    elif usr.password != __hashPassword__(password):
        raise HTTPException(status_code=400, detail="密码错误")
    usr.password = None
    return {'usr': dict(usr)}


def userHistory(uid):
    userAnimeHistoryList = getAnimeHistoryByUserId(uid)
    userComicHistoryList = getComicHistoryByUserId(uid)
    userNovelHistoryList = getNovelHistoryByUserId(uid)
    id = []
    cover = []
    title = []
    timestamp = []
    for animeHistory in userAnimeHistoryList:
        anime = getAnimeById(animeHistory.aid)
        id.append(animeHistory.aid)
        timestamp.append(animeHistory.timestamp)
        cover.append(anime.cover)
        title.append(anime.title)
    for comicHistory in userComicHistoryList:
        comic = getComicById(comicHistory.cid)
        id.append(comicHistory.cid)
        timestamp.append(comicHistory.timestamp)
        cover.append(comic.cover)
        title.append(comic.title)
    for novelHistory in userNovelHistoryList:
        novel = getNovelById(novelHistory.nid)
        id.append(novelHistory.nid)
        timestamp.append(novelHistory.timestamp)
        cover.append(novel.cover)
        title.append(novel.title)
    # 封面 id 标题 按照时间戳排序

    return {'result': {'id': id, 'title': title, 'cover': cover, 'timestamp': timestamp}}


# TEST
'''
单元测试：
  usrLogin()
'''
if __name__ == '__main__':
    print(usrLogin(1000, '123456'))
    print(userHistory(1025))
