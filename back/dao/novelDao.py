#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/24 9:26
@Author: Jocx,WILLOSCAR
@Description:
    对小说表单的操作
'''

import traceback

from bean.novelBean import NovelBean
from dao.utils import database


def getNovel():
    r"""获得nid升序的NovelBean列表"""
    conn, cursor = database()
    table_name = "novel"
    attr = "nid"
    sql = f"""
            SELECT * 
            FROM {table_name} 
            order by  {attr}      
            """
    novels = []
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            novels.append(NovelBean(
                nid=row[0],
                url=row[1],
                cover=row[2],
                title=row[3],
                author=row[4],
                score=row[5],
                type=row[6],
                depth=row[7],
                state=row[8],
                click_cnt=row[9],
                update_time=row[10],
                introduce=row[11]
            ))
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return novels


def getNovelById(nid):
    r"""根据nid获得一个具体的NovelBean"""
    conn, cursor = database()
    table_name = "novel"
    selId = "nid"
    sql = f"""
                SELECT * 
                FROM {table_name}  
                where  {selId}={nid}   
                """
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        novel_bean = NovelBean(
                nid=row[0],
                url=row[1],
                cover=row[2],
                title=row[3],
                author=row[4],
                score=row[5],
                type=row[6],
                depth=row[7],
                state=row[8],
                click_cnt=row[9],
                update_time=row[10],
                introduce=row[11]
            )
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        return None
    return novel_bean


# TEST
'''
单元测试：
  getNovel()
  getNovelById()
'''
if __name__ == '__main__':
    print(len(getNovel()))
    print(getNovelById('31'))
