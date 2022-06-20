import json
import codecs
import os
import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库

num2str = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

def getStopWords(stopWords_filePath):
    stopwords = [line.strip() for line in open(stopWords_filePath, 'r', encoding='utf-8').readlines()]
    return stopwords

if __name__ == '__main__':
    with open("../data/comic.json", encoding="utf-8") as file:
        file_json = json.load(file)
    text = ""
    for line in file_json:
        text += line['title']

    #分词
    cut = jieba.cut(text)
    string = ' '.join(cut)

    img = Image.open(r'.\src\蒙版2.jpg')   #打开遮罩图片
    img_array = np.array(img)   #将图片转换为数组
    stopwords = getStopWords(r'src\stop_words.txt')
    stopwords += ["港澳台", "地区", "第二季", "地區", "台灣", "僅限", "剧场版", "第一季", "第三季"]
    for i in range(9):
        stopwords.append("十" + num2str[i])
        stopwords.append(num2str[i] + "十")
    for i in range(1, 9):
        for j in range(9):
            stopwords.append(num2str[i] + "十" + num2str[j])
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path="msyh.ttc",    #字体所在位置：C:\Windows\Fonts
        stopwords = stopwords
    )
    wc.generate_from_text(string)


    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')     #是否显示坐标轴

    plt.show()    #显示生成的词云图片

    #输出词云图片到文件
    wc.to_file("../image/comic_title.png")