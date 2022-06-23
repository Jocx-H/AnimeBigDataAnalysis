#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 9:41
# @Author: Jocx
# @Description:
#   前端调用的获取热门动漫、小说、漫画、cosplay按热度降序排序的API

import traceback
from fastapi import APIRouter, Query, Path, HTTPException
from fastapi.encoders import jsonable_encoder

from action.msgCodeConfig import Code400
from service import hotRecomService


# 构建api路由
router = APIRouter(
    prefix="/hot",
    tags=["HotRecommend"],
)


@router.get("/anime", responses={400: {"model": Code400}})
async def getAnime():
    r"""
    按热度升序获得热门动漫数据
    """
    try:
        hotAnime = hotRecomService.getAnime()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(hotAnime)


@router.get("/novel", responses={400: {"model": Code400}})
async def getNovel():
    r"""
    按热度降序获得热门小说数据
    """
    try:
        hotNovel = hotRecomService.getAnime()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(hotNovel)


@router.get("/comic", responses={400: {"model": Code400}})
async def getComic():
    r"""
    按热度降序获得热门漫画数据
    """
    try:
        hotComic = hotRecomService.getAnime()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(hotComic)


@router.get("/cosplay", responses={400: {"model": Code400}})
async def getCosplay():
    r"""
    按热度降序获得热门cosplay数据
    """
    try:
        hotCosplay = hotRecomService.getAnime()
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(hotCosplay)
