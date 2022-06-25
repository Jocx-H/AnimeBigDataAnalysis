#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:42
@Author: Jocx,WILLOSCAR
@Description:
  提供给热门推荐API的服务，包括：
      按热度降序排序动漫、小说、漫画和cosplay
'''

from dao import animeDao, comicDao, novelDao, cosplayDao


def __statAnime__():
    r"""
    统计并按照热度排序动漫
    """
    return animeDao.getAnime()


def __statNovel__():
    r"""
    统计并按照热度排序小说
    """
    return novelDao.getNovel()


def __statComic__():
    r"""
    统计并按照热度排序漫画
    """
    return comicDao.getComic()


def __statCosplay__():
    r"""
    统计并按照热度排序cosplay
    """
    return cosplayDao.getCosplay()


def getAnime() -> dict:
    return {'result': __statAnime__()}


def getNovel() -> dict:
    return {'result': __statNovel__()}


def getComic() -> dict:
    return {'result': __statComic__()}


def getCosplay() -> dict:
    return {'result': __statCosplay__()}
