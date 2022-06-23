#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 17:08
# @Author: Jocx
# @Description: 数据表单`用户cosplay浏览记录`的抽象类


from dataclasses import dataclass


@dataclass(order=False)
class UserCosplayHistoryBean:
    coshid: int
    uid: int
    cosid: int
    score: float = None
    ratio: float = None
    like: bool = None
    collect: bool = None
    timestamp: str = None  # TODO 请在使用前将str改为与MySQL Date数据适配的类型
