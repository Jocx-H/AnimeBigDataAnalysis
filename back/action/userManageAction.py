#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:41
@Author: Jocx
@Description:
'''

import traceback
from fastapi import APIRouter, Query, Path, HTTPException
from fastapi.encoders import jsonable_encoder

from action.msgCodeConfig import Code400
from service import userManageService


# 构建api路由
router = APIRouter(
    prefix="/user",
    tags=["userManage"],
)


@router.post("/login", responses={400: {"model": Code400}})
def usrLogin(account: str, password: str):
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
