#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 17:07
@Author: Jocx
@Description: 数据表单`漫画`的抽象类
'''


from dataclasses import dataclass


@dataclass(order=False)
class ComicBean:
    cid: int
    url: str = None
    cover: str = None
    title: str = None
    last_short_title: str = None
    author: str = None
    type: str = None
    state: str = None

    def keys(self):
        return 'cid', 'url', 'cover', 'title', 'last_short_title', 'author', 'type', 'state'

    def __getitem__(self, item):
        return getattr(self, item)