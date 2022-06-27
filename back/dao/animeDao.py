#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx ,WILLOSACR
@Description:
    对动漫表单的操作
'''

import traceback

from bean.animeBean import AnimeBean
from dao.utils import database


def getAnime():
    r"""获得以aid升序的AnimeBean列表"""
    conn, cursor = database()
    table_name = "anime"
    attr = "aid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            ORDER BY {attr}
            """
    animes = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            animes.append(AnimeBean(
                aid=row[0],
                title=row[1],
                index_show=row[2],
                is_finished=row[3],
                video_link=row[4],
                cover=row[5],
                pub_real_time=row[6],
                renewal_time=row[7],
                favorites=row[8],
                coins=row[9],
                views=row[10],
                danmakus=row[11],
                depth=row[12],
                media_tags=row[13],
                score=row[14],
                cm_count=row[15]
            ))
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return animes


def getAnimeById(aid):
    r"""根据aid获得一个具体的AnimeBean"""
    conn, cursor = database()
    table_name = "anime"
    selId = "aid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            where {selId}={aid}
            """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        anime_bean = AnimeBean(
            aid=row[0],
            title=row[1],
            index_show=row[2],
            is_finished=row[3],
            video_link=row[4],
            cover=row[5],
            pub_real_time=row[6],
            renewal_time=row[7],
            favorites=row[8],
            coins=row[9],
            views=row[10],
            danmakus=row[11],
            depth=row[12],
            media_tags=row[13],
            score=row[14],
            cm_count=row[15])
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return anime_bean


# TEST
'''
单元测试：
  getAnime()
  getAnimeById()
'''
if __name__ == '__main__':
    print(len(getAnime()))
    print(getAnimeById(11))