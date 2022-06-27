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
from animeDao import getAnime, getAnimeById
from comicDao import getComic, getComicById
from novelDao import getNovel, getNovelById
from cosplayDao import getCosplay, getCosplayById

if __name__ == '__main__':
    novel = getNovelById(3298)
    # getAnime()
    # getComic()
    # getNovel()
    # getCosplay()
