#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time: 2022/6/23 9:43
@Author: Jocx
@Description:
    提供给用户管理API的服务，包括：
        对用户的登录信息进行验证
'''


from fastapi import HTTPException
from hashlib import md5


def __hashPassword__(password: str):
    r"""
    hd5加密密码
    """
    usrHash = md5()
    usrHash.update(password.encode(encoding='utf-8'))
    return usrHash.hexdigest()


def usrLogin(username: str, password: str) -> dict:
    r"""
    检查用户账号和密码是否与数据库中账号密码匹配
    """
    if len(username) > 50 or len(password) > 50:
        raise HTTPException(status_code=400, detail="无效的用户名或密码")
    #
    # 访问数据库获得用户数据usr，usr是一个usrBean类
    #
    usr = {}  # TODO 这里在实际编写的时候需要用Dao包里面的方法请求数据库，且usr应该是一个usrBean类
    if usr is None:
        raise HTTPException(status_code=400, detail="查无此人")
    else:
        usrInfo = dict(usr)
        if usrInfo['password'] != __hashPassword__(password):
            raise HTTPException(status_code=400, detail="密码错误")
    del usrInfo['password']
    return {'usr': usrInfo}
