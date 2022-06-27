#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx,WILLOSACR
@Description:
'''
from utils import database


def getComic():
    conn, cursor = database()
    table_name = "comic"
    attr = "cid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            order by  {attr}
            """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)
    # conn.commit()

def getComicById(id):
    conn, cursor = database()
    table_name = "comic"
    attr = "cid"
    selId = "cid="
    sql = f"""
                SELECT * 
                FROM {table_name} 
                where  {selId}{id}   
                """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)