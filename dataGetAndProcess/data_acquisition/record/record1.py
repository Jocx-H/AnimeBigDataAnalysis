import numpy
import random
import pandas
import time
import json

# 生成近期观影记录
'''
id : int
recentRecord : list[map] map:{data:[id]}

'''
userId = [_ for _ in range(1, 1001)]
random.shuffle(userId)
print(userId)
timestamp = time.time()
Day = 24 * 3600
timeList = []
strfTimeList = []
animeMaxNum = 3531
comicMaxNum = 20931
novelMaxNum = 9841
recordDict = dict()
for user in userId:
    recordDict[user] = []
    for i in range(1, 8):
        randomList = [random.randint(1, 3) for l in range(random.randint(10, 15))]
        strRandomList = map(lambda x: str(x), randomList)
        # print(strRandomList)
        strRandomList = "".join(strRandomList)
        print(strRandomList)
        recordID = []
        for typeRecord in randomList:
            if typeRecord == 1:
                recordID.append(int('1' + str(random.randint(1, animeMaxNum))))
            elif typeRecord == 2:
                recordID.append(int('2' + str(random.randint(1, comicMaxNum))))
            elif typeRecord == 3:
                recordID.append(int('3' + str(random.randint(1, novelMaxNum))))

        timeCheck = time.asctime(time.localtime(timestamp))
        strTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        strTime = strTime[0:10]
        recordDict[user].append({strTime: strRandomList})
        timeList.append(timeCheck)
        strfTimeList.append(strTime)
        timestamp -= Day
        t = time.asctime()

with open("record1.json", "w", encoding='utf-8') as f:
    # json.dump(dict_, f)  # 写为一行
    json.dump(recordDict, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
