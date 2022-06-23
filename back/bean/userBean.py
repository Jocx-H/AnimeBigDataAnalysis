#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/6/23 16:36
# @Author: Jocx
# @Description: 数据表单`用户`的抽象类


from dataclasses import dataclass


@dataclass(order=False)
class UserBean:
    uid: int
    uname: str = None
    password: str = None
