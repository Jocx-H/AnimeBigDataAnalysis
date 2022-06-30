#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 17:08
@Author: Jocx, CloudAndMist
@Description: 数据表单`用户小说浏览记录`的抽象类
'''


from dataclasses import dataclass


@dataclass(order=False)
class UserNovelHistoryBean:
    nhid: int
    uid: int
    nid: int
    score: float = None
    ratio: float = None
    like: bool = None
    collect: bool = None
    timestamp: int = None

    def __post_init__(self):
        self.historyid = self.nid