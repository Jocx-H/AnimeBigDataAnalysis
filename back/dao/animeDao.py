#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx ,WILLOSACR
@Description:
'''
import pymysql
import prettytable as pt
import json
import time
from pymysql.converters import escape_string
from utils import database


def getAnime():
    conn, cursor = database()
    table_name = "anime"
    attr = "aid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            ORDER BY   {attr}
            """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)
    # conn.commit()

def getAnimeById(id):
    conn, cursor = database()
    table_name = "anime"
    attr = "aid"
    selId = "aid="
    sql = f"""
                SELECT * 
                FROM {table_name} 
                order by {attr} 
                where  {selId}{id}   
                """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)