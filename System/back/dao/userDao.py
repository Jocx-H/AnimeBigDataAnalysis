#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx, CloudAndMist
@Description:
'''

import traceback

from dao.utils import database
from bean.userBean import UserBean


def getUserById(userId: int):
    conn, cursor = database()
    table_name = "user"
    sql = f"""
            SELECT * 
            FROM {table_name}
            WHERE uid = {userId}
            """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        usr = UserBean(
            uid=row[0],
            uname=row[1],
            password=row[2]
        )
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return usr


if __name__ == '__main__':
    print(getUserById(1000))
