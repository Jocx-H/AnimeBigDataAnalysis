#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 17:07
@Author: Jocx
@Description: 数据表单`动漫`的抽象类
'''

from dataclasses import dataclass


@dataclass(order=False)
class AnimeBean:
    aid: int
    title: str = None
    index_show: str = None
    is_finished: bool = None
    video_link: str = None
    cover: str = None
    pub_real_time: int = None
    renewal_time: int = None
    favorites: int = None
    coins: int = None
    views: int = None
    danmakus: int = None
    depth: int = None
    media_tags: str = None
    score: float = None
    cm_count: str = None

    def keys(self):
        return 'aid', 'title', 'index_show', 'is_finished', 'video_link', 'cover', 'pub_real_time', \
               'renewal_time', 'favorites', 'coins', 'views', 'danmakus', 'depth', 'media_tags', 'score', 'cm_count'

    def __getitem__(self, item):
        return getattr(self, item)
