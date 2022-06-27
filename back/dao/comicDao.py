#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx,WILLOSACR
@Description:
    对漫画表单的操作
'''

import traceback

from bean.comicBean import ComicBean
from dao.utils import database


def getComic():
    r"""获得以cid升序的ComicBean列表"""
    conn, cursor = database()
    table_name = "comic"
    attr = "cid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            order by  {attr}
            """
    comics = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            comics.append(ComicBean(
                cid=row[0],
                url=row[1],
                cover=row[2],
                title=row[3],
                last_short_title=row[4],
                author=row[5],
                type=row[6],
                state=row[7]
            ))
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return comics


def getComicById(cid):
    r"""根据cid获得一个具体的ComicBean"""
    conn, cursor = database()
    table_name = "comic"
    attr = "cid"
    selId = "cid"
    sql = f"""
                SELECT * 
                FROM {table_name} 
                where {selId}={cid}   
                """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        comic_bean = ComicBean(
            cid=row[0],
            url=row[1],
            cover=row[2],
            title=row[3],
            last_short_title=row[4],
            author=row[5],
            type=row[6],
            state=row[7]
        )
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return comic_bean


# TEST
'''
单元测试：
  getComic()
  getComicById()
'''
if __name__ == '__main__':
    print(len(getComic()))
    print(getComicById(21))
