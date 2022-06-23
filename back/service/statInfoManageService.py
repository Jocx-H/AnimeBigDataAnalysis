#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 9:42
# @Author: Jocx
# @Description:
#   提供给统计信息API的服务，包括：
#       统计各阶段分数
#       统计不同类型标签的各种信息
#       统计各个作品的关键词


def __animeScoreStatInfo__():
    r"""
    统计全站动漫的分数信息
    """
    pass


def __novelScoreStatInfo__():
    r"""
    统计全站小说的分数信息
    """
    pass


def __animeTypeStatInfo__():
    r"""
    统计全站动漫的类型信息
    """
    pass


def __novelTypeStatInfo__():
    r"""
    统计全站小说的类型信息
    """
    pass


def __comicTypeStatInfo__():
    r"""
    统计全站漫画的类型信息
    """
    pass


def __animeKeyWordStatInfo__():
    r"""
    统计全站动漫的关键词信息
    """
    pass


def __novelKeyWordStatInfo__():
    r"""
    统计全站小说的关键词信息
    """
    pass


def __comicKeyWordStatInfo__():
    r"""
    统计全站漫画的关键词信息
    """
    pass


def __cosplayKeyWordStatInfo__():
    r"""
    统计全站cosplay的关键词信息
    """
    pass


def getAnimeScore() -> dict:
    return {'result': __animeScoreStatInfo__()}


def getNovelScore() -> dict:
    return {'result': __novelScoreStatInfo__()}


def getAnimeType() -> dict:
    return {'result': __animeTypeStatInfo__()}


def getNovelType() -> dict:
    return {'result': __novelTypeStatInfo__()}


def getComicType() -> dict:
    return {'result': __comicTypeStatInfo__()}


def getAnimeKeyWord() -> dict:
    return {'result': __animeKeyWordStatInfo__()}


def getNovelKeyWord() -> dict:
    return {'result': __novelKeyWordStatInfo__()}


def getComicKeyWord() -> dict:
    return {'result': __comicKeyWordStatInfo__()}


def getCosplayKeyWord() -> dict:
    return {'result': __cosplayKeyWordStatInfo__()}


