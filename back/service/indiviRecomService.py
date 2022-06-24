#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:42
@Author: Jocx
@Description:
  提供给个性化推荐API的服务，包括：
      按用户喜好程度降序排序动漫、小说、漫画
'''


def __computeAnime__(uname: str):
    r"""
    根据推荐算法计算出用户喜爱的动漫
    """
    pass


def __computeNovel__(uname: str):
    r"""
    根据推荐算法计算出用户喜爱的小说
    """
    pass


def __computeComic__(uname: str):
    r"""
    根据推荐算法计算出用户喜爱的漫画
    """
    pass


def getAnime(uname: str):
    return {'result': __computeAnime__(uname)}


def getNovel(uname: str):
    return {'result': __computeNovel__(uname)}


def getComic(uname: str):
    return {'result': __computeComic__(uname)}
