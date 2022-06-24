#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:39
@Author: Jocx
@Description:
  前端调用的获取个性化推荐的动漫、小说、漫画按用户喜好程度降序排序的API
'''

import traceback
from fastapi import APIRouter, Query, Path, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import Field

from action.msgCodeConfig import Code400
from service import indiviRecomService

# 构建api路由
router = APIRouter(
    prefix="/indivi",
    tags=["indiviRecommend"],
)


@router.post("/anime", responses={400: {"model": Code400}})
def getAnime(uname: str = Field(None, min_length=1, max_length=50)):
    r"""
    根据用户喜好个性化推荐动漫
    """
    try:
        indiviAnime = indiviRecomService.getAnime(uname)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(indiviAnime)


@router.post("/novel", responses={400: {"model": Code400}})
def getNovel(uname: str = Field(None, min_length=1, max_length=50)):
    r"""
    根据用户喜好个性化推荐小说
    """
    try:
        indiviNovel = indiviRecomService.getNovel(uname)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(indiviNovel)


@router.post("/comic", responses={400: {"model": Code400}})
def getComic(uname: str = Field(None, min_length=1, max_length=50)):
    r"""
    根据用户喜好个性化推荐漫画
    """
    try:
        indiviComic = indiviRecomService.getComic(uname)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(indiviComic)