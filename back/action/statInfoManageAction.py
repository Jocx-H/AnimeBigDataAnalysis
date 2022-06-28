#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:42
@Author: Jocx
@Description:
  获取动漫、小说、漫画和cosplay各项统计信息的API
  统计信息包括：
      动漫、小说的分数；
      动漫、小说、漫画的类型；
      动漫、小说、漫画、cosplay的关键词
'''

import traceback
from fastapi import APIRouter, Query, Path, HTTPException
from fastapi.encoders import jsonable_encoder

from action.msgCodeConfig import Code400
from service import statInfoManageService


# 构建api路由
router = APIRouter(
    prefix="/stat",
    tags=["statInfo"],
)


@router.get("/animescore", responses={400: {"model": Code400}})
def getAnimeScore():
    r"""
    获得全站动漫分数的统计信息
    """
    try:
        animeScore = statInfoManageService.getAnimeScore()
        if animeScore['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(animeScore)


@router.get("/novelscore", responses={400: {"model": Code400}})
def getNovelScore():
    r"""
    获得全站小说分数的统计信息
    """
    try:
        novelScore = statInfoManageService.getNovelScore()
        if novelScore['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(novelScore)


@router.get("/animetype", responses={400: {"model": Code400}})
def getAnimeType():
    r"""
    获得全站动漫类型的统计信息
    """
    try:
        animeType = statInfoManageService.getAnimeType()
        if animeType['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(animeType)


@router.get("/noveltype", responses={400: {"model": Code400}})
def getNovelType():
    r"""
    获得全站动漫小说类型的统计信息
    """
    try:
        novelType = statInfoManageService.getNovelType()
        if novelType['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(novelType)


@router.get("/comictype", responses={400: {"model": Code400}})
def getComicType():
    r"""
    获得全站漫画类型的统计信息
    """
    try:
        comicType = statInfoManageService.getComicType()
        if comicType['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(comicType)


@router.get("/animekeyword", responses={400: {"model": Code400}})
def getAnimeKeyWord():
    r"""
    获得全站动漫关键词的统计信息
    """
    try:
        animeKeyWord = statInfoManageService.getAnimeKeyWord()
        if animeKeyWord['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(animeKeyWord)


@router.get("/novelkeyword", responses={400: {"model": Code400}})
def getNovelKeyWord():
    r"""
    获得全站小说关键词的统计信息
    """
    try:
        novelKeyWord = statInfoManageService.getNovelKeyWord()
        if novelKeyWord['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(novelKeyWord)


@router.get("/comickeyword", responses={400: {"model": Code400}})
def getComicKeyWord():
    r"""
    获得全站漫画关键词的统计信息
    """
    try:
        comicKeyWord = statInfoManageService.getComicKeyWord()
        if comicKeyWord['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(comicKeyWord)


@router.get("/cosplaykeyword", responses={400: {"model": Code400}})
def getCosplayKeyWord():
    r"""
    获得全站cosplay关键词的统计信息
    """
    try:
        cosplayKeyWord = statInfoManageService.getCosplayKeyWord()
        if cosplayKeyWord['result'] is None:
            raise HTTPException(status_code=400, detail="没有获取相关数据")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(cosplayKeyWord)


