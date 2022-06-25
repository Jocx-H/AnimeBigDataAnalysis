#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx,WILLOSACR
@Description:
'''

import pymysql
import prettytable as pt
import json
import time
from pymysql.converters import escape_string
from utils import database


def getCosplay():
    conn, cursor = database()
    table_name = "cosplay"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)
    # conn.commit()