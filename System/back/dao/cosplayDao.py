#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:27
@Author: Jocx,WILLOSACR
@Description:
    对cosplay表单的操作
'''

import traceback

from bean.cosplayBean import CosplayBean
from dao.utils import database


def getCosplay():
    r"""获得nid升序的CosplayBean列表"""
    conn, cursor = database()
    table_name = "cosplay"
    attr = "cosid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            order by  {attr} 
            """
    cosplays = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            cosplays.append(CosplayBean(
                cosid=row[0],
                url=row[1],
                cover=row[2],
                title=row[3],
            ))
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return cosplays


def getCosplayById(cosid):
    r"""根据cosid获得一个具体的CosplayBean"""
    conn, cursor = database()
    table_name = "cosplay"
    attr = "cosid"
    selId = "cosid"
    sql = f"""
                SELECT * 
                FROM {table_name}  
                where  {selId}={cosid}   
                """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        cosplay_bean = CosplayBean(
                cosid=row[0],
                url=row[1],
                cover=row[2],
                title=row[3],
            )
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return cosplay_bean


def getCosplayDict():
    r"""获得nid升序的CosplayBean字典"""
    conn, cursor = database()
    table_name = "cosplay"
    attr = "cosid"
    sql = f"""
            SELECT cosid,cover,title 
            FROM {table_name} 
            order by  {attr} 
            """
    cosplays_dict = {}
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            cosplays_dict[row[0]] = dict(CosplayBean(
                cosid=row[0],
                cover=row[1],
                title=row[2],
            ))
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return cosplays_dict


# TEST
'''
单元测试：
  getCosplay()
  getCosplayById()
  getCosplayDict()
'''
if __name__ == '__main__':
    print(len(getCosplay()))
    print(getCosplayById('41'))
    print(getCosplayDict())
