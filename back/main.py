#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# @Time: 2022/6/23 9:39
# @Author: 何润熹
# @Description: 二次元动漫推荐系统主程序，用于开发环境的调试
'''

import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from action import hotRecomAction, statInfoManageAction, userManageAction, indiviRecomAction

# 声明fastapi的实例
app = FastAPI(title='文档说明', description='整体描述')

# 配置静态资源的存放路径以及请求的路径
app.mount("/resources", StaticFiles(directory="assets/public"), name="assets/public")

# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


# 注册api模块
app.include_router(hotRecomAction.router, prefix='/api')
app.include_router(indiviRecomAction.router, prefix='/api')
app.include_router(userManageAction.router, prefix='/api')
app.include_router(statInfoManageAction.router, prefix='/api')


# 配置容器启动相应的实例
if __name__ == '__main__':
    uvicorn.run(app='main:app', port=80, reload=True, debug=True)
