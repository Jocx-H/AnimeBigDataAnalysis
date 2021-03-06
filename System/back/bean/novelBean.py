#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 17:07
@Author: Jocx
@Description: 数据表单`小说`的抽象类
'''


from dataclasses import dataclass


@dataclass(order=False)
class NovelBean:
    nid: int
    url: str = None
    cover: str = None
    title: str = None
    author: str = None
    score: float = None
    type: str = None
    depth: int = None
    state: str = None
    click_cnt: int = None
    update_time: str = None
    introduce: str = None
    cm_count: str = None

    def keys(self):
        return 'nid', 'url', 'cover', 'title', 'author', 'score', 'type', 'depth', 'state', 'click_cnt', \
               'update_time', 'introduce'

    def __getitem__(self, item):
        return getattr(self, item)
