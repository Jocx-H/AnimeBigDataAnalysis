#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx,WILLOSCAR
@Description:
'''

import pymysql
import prettytable as pt
import json
import time
from pymysql.converters import escape_string
from utils import database


def getNovel():
    conn, cursor = database()
    table_name = "novel"
    attr = "nid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            order by {attr}      
            """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)
    # conn.commit()
