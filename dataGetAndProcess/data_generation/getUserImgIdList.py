# -*- codeing = utf-8 -*-
# @Time :2022/6/23 16:34
# @File : getUserImgIdList.py
# @author: derrick

import json

'''
用户画像tag表:
中二、现充、肥宅、志怪、青春
'''
# 中二
str = "热血，战斗，冒险，魔法，运动，机战，励志，冒险，热血，格斗，魔法，励志，战争，竞技，武侠，魔幻，校园"
zhonger = str.split('，')
zhongerTagSet = set(zhonger)

# 现充
str = "搞笑，校园，治愈，职场，历史，美食，生活，职场，美食，欢乐向，战争，历史，都市"
xianchong = str.split('，')
xianchongTagSet = set(xianchong)

# 肥宅
str = "萌系，少女，穿越，偶像，音乐，泡面，萝莉，秀吉，宅系，萌系，福瑞，舰娘，音乐舞蹈，同人"
feizhai = str.split('，')
feizhaiTagSet = set(feizhai)

# 志怪
str = "奇幻，科幻，架空，魔法，神魔，小说改，推理，奇幻，科幻，悬疑，魔法，神鬼，仙侠，惊悚，魔幻，恐怖，古风，玄幻，悬疑"
zhiguai = str.split('，')
zhiguaiTagSet = set(zhiguai)

# 青春
str = "日常，校园，恋爱，冒险，励志，社团，爱情，校园，纯爱，励志，校园，都市"
qingchun = str.split('，')
qingchunTagSet = set(qingchun)


'''
根据用户画像tag表，获取对应种类作品的id列表
'''
# 动漫
def getAnimeIdBasedOnTags(tagSet: set) -> list:
    animeTagIdList = []
    cnt = 0
    with open("../data/anime.json", encoding ="utf-8") as file:
        file_json = json.load(file)
    for line in file_json:
        cnt = 0
        for tag in line['media_tags']:
            if tag in tagSet:
                cnt += 1
                if(cnt == 2):
                    animeTagIdList.append(line['id'])
                    break
    return animeTagIdList

# 漫画
def getComicIdBasedOnTags(tagSet: set) -> list:
    comicTagIdList = []
    cnt = 0
    with open("../data/comic.json", encoding ="utf-8") as file:
        file_json = json.load(file)
    for line in file_json:
        cnt = 0
        for tag in line['type']:
            if tag in tagSet:
                cnt += 1
                if(cnt == 2):
                    comicTagIdList.append(line['id'])
                    break
    return comicTagIdList

# 小说
def getNovelIdBasedOnTags(tagSet: set) -> list:
    novelTagIdList = []
    with open("../data/novel.json", encoding ="utf-8") as file:
        file_json = json.load(file)
    for line in file_json:
        for tag in tagSet:
            if tag == line['type']:
                novelTagIdList.append(line['id'])
    return novelTagIdList

# cosplay(实际上cosplay无tag，不基于画像甄别，返回全部id)
def getCosIdBasedOnTags(tagSet: set) -> list:
    cosTagIdList = []
    with open("../data/cos.json", encoding ="utf-8") as file:
        file_json = json.load(file)
    for line in file_json:
        cosTagIdList.append(line['id'])
    return cosTagIdList

# 测试代码
# print(len(getNovelIdBasedOnTags(qingchunTagSet)))

# 保存各个画像对应的selectList以提高速度：空间换时间
tagSet = qingchunTagSet
imgList = []
animeList = getAnimeIdBasedOnTags(tagSet)
comicList = getComicIdBasedOnTags(tagSet)
novelList = getNovelIdBasedOnTags(tagSet)
cosList = getCosIdBasedOnTags(tagSet)
imgList = [animeList, comicList, novelList, cosList]
# 写入json文件中（多行写入）
with open("qingchunSelectList.json", "w", encoding='utf-8') as f:
    json.dump(imgList, f, indent = 2, sort_keys = True, ensure_ascii = False)
print('write into json completed!')