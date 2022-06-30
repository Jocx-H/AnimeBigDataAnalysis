#!/bin/sh

###################################### 
# @Author: Jocx
# @Time: 2022-6-14
# @Description: 部署环境自动配置文件
######################################

conda activate base
pip3 install PyMySQL -i https://pypi.tuna.tsinghua.edu.cn/simple
echo PyMySQL安装完毕
pip3 install fastapi -i https://pypi.tuna.tsinghua.edu.cn/simple
echo fastapi安装完毕
pip3 install uvicorn -i https://pypi.tuna.tsinghua.edu.cn/simple
echo uvicorn安装完毕
pip3 install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
echo pandas安装完毕
pip3 install jieba -i https://pypi.tuna.tsinghua.edu.cn/simple
echo jieba安装完毕