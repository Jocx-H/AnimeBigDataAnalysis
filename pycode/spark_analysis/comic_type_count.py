from pyspark import SparkConf, SparkContext
import json
import codecs
import os

if __name__ == '__main__':
    #conf = SparkConf().setMaster("spark://Pspark:7077").setAppName("rdd-1")
    conf = SparkConf().setMaster("local[2]").setAppName("rdd-1")
    sc = SparkContext(conf=conf)
    with open("../data/comic.json", encoding="utf-8") as file:
        file_json = json.load(file)
    # 将每line的所有标签添加进data中
    data = []
    for line in file_json:
        for i in line['type']:
            data.append(i)
    rdd1 = sc.parallelize(data)
    counts = rdd1.map(lambda x:(x, 1)) \
            .reduceByKey(lambda a,b:a+b) \
            .map(lambda x:(x[1], x[0])) \
            .sortByKey(False) \
            .map(lambda x:(x[1], x[0]))
    output = counts.collect()
    for (word,count) in output:
        print("%s: %i" % (word,count))

    sc.stop()
