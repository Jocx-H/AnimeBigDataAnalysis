"""
@Author: CloudAndMist
"""
import json
import codecs
import os
import jieba        #分词
from pyspark import SparkConf, SparkContext

# 读取停词表
def getStopWords(stopWords_filePath):
    stopwords = [line.strip() for line in open(stopWords_filePath, 'r', encoding='utf-8').readlines()]
    return stopwords

if __name__ == '__main__':
    with open("../data/preData/preNovel.json", encoding="utf-8") as file:
        file_json = json.load(file)
    text = ""
    for line in file_json:
        text += line['title']

    #分词
    cut = jieba.cut(text)
    cut_string = ' '.join(cut)
    cut_list = jieba.lcut(text)

    # 停词表生成
    stopwords = getStopWords(r'src\stop_words.txt')
    stopwords += ["港澳台", "地区", "第二季", "地區", "OVA", "台灣", "僅限", "剧场版", "第一季", "第三季", "篇", " ", "新",
                  "季", "哆", "版", "名", "号", "部", "记", "达", " ", "事", "里", "女", "成", "提", "约", "做", "想"
                  "中"]

    stop_list = [word for word in cut_list if word not in stopwords]

    # spark 统计词频
    conf = SparkConf().setMaster("local[2]").setAppName("rdd-1")
    sc = SparkContext(conf=conf)
    rdd1 = sc.parallelize(stop_list)
    counts = rdd1.map(lambda x:(x, 1)) \
            .reduceByKey(lambda a,b:a+b) \
            .map(lambda x:(x[1], x[0])) \
            .sortByKey(False) \
            .map(lambda x:(x[1], x[0]))
    output = counts.collect()
    json_file = codecs.open('../data/preData/pre_novel_title_count.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    for (word, count) in output:
        print("%s: %i" % (word, count))
        item_json = json.dumps({'word': word, 'count': count}, ensure_ascii=False)
        json_file.write('\t' + item_json + ',\n')
    json_file.seek(-2, os.SEEK_END)
    # 使用 truncate() 方法，将后面的数据清空
    json_file.truncate()
    # 重新输出'\n'，并输入']'，与 open_spider(self, spider) 时输出的 '['，构成一个完整的数组格式
    json_file.write('\n]')
    sc.stop()



