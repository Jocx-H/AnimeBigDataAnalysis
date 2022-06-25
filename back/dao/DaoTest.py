#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: DaoTest.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 25, 2022
# ---
# 测试Dao文件
from animeDao import getAnime
from comicDao import getComic
from novelDao import getNovel
from cosplayDao import getCosplay
if __name__ == '__main__':
    getAnime()
    getComic()
    getNovel()
    getCosplay()