#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx, CloudAndMist
@Description:
'''

from utils import database

def getUserById(userId: int):
    conn, cursor = database()
    table_name = "user"
    sql = f"""
            SELECT * 
            FROM {table_name}
            WHERE uid = {userId}
            """
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(list(res))
    return list(res)