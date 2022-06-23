#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 17:21
# @Author: Jocx
# @Description: 数据表单`cosplay`的抽象类


from dataclasses import dataclass


@dataclass(order=False)
class CosplayBean:
    cosid: int
    url: str = None
    cover: str = None
    title: str = None
