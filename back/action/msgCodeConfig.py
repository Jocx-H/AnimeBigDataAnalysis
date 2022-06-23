#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 15:07
# @Author: Jocx
# @Description: 配置各种状态码返回的信息

from pydantic import BaseModel


class Code400(BaseModel):
    detail: str = "客户端运行错误，请检查输入内容或联系管理员！"


class Code403(BaseModel):
    detail: str = "客户端请求权限不足"
