#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:41
@Author: Jocx, CloudAndMist
@Description: 提供给用户管理相关的各种API
'''

import traceback
from fastapi import APIRouter, Query, Path, HTTPException
from fastapi.encoders import jsonable_encoder

from action.msgCodeConfig import Code400
from service import userManageService
from service import userAnalysisService

# 构建api路由
router = APIRouter(
    prefix="/user",
    tags=["userManage"],
)


@router.post("/login", responses={400: {"model": Code400}})
def usrLogin(account: int, password: str):
    r"""
    返回用户登录信息
    """
    try:
        loginResult = userManageService.usrLogin(account, password)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(loginResult)


@router.post("/analysis", responses={400: {"model": Code400}})
def usrLogin(uid: int):
    r"""
    返回用户登录信息
    """
    try:
        analysisResult = userAnalysisService.userAnalysis(uid)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(analysisResult)


@router.post("/history", responses={400: {"model": Code400}})
def usrHistory(uid: int):
    r"""
    返回用户登录信息
    """
    try:
        historyResult = userManageService.userHistory(uid)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(repr(e))
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="客户端运行错误，请检查输入内容或联系管理员！")
    return jsonable_encoder(historyResult)
