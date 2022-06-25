"""
@Author: CloudAndMist
"""
from pyspark import SparkConf, SparkContext
import json
import codecs
import os

if __name__ == '__main__':
    #conf = SparkConf().setMaster("spark://Pspark:7077").setAppName("rdd-1")
    conf = SparkConf().setMaster("local[2]").setAppName("rdd-1")
    sc = SparkContext(conf=conf)
    with open("../data/preData/preAnime.json", encoding="utf-8") as file:
        file_json = json.load(file)
    # 将每line的所有标签添加进data中
    data = []
    for line in file_json:
        for i in line['media_tags']:
            data.append(i)
    rdd1 = sc.parallelize(data)
    counts = rdd1.map(lambda x:(x, 1)) \
            .reduceByKey(lambda a,b:a+b) \
            .map(lambda x:(x[1], x[0])) \
            .sortByKey(False) \
            .map(lambda x:(x[1], x[0]))
    output = counts.collect()
    json_file = codecs.open('../data/anime_type_count.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    for (word,count) in output:
        print("%s: %i" % (word,count))
        item_json = json.dumps({'type': word, 'count': count}, ensure_ascii=False)
        json_file.write('\t' + item_json + ',\n')
    json_file.seek(-2, os.SEEK_END)
    # 使用 truncate() 方法，将后面的数据清空
    json_file.truncate()
    # 重新输出'\n'，并输入']'，与 open_spider(self, spider) 时输出的 '['，构成一个完整的数组格式
    json_file.write('\n]')
    sc.stop()
