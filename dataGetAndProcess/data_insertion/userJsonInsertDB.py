# -*- coding = utf-8 -*-
# @Time : 2022/6/27 9:19
# @File : userJsonInsertDB.py
# @Author : derrick

import pymysql
import json

sysDataList = []

def insertUserJsonToDB(userId: int):
    global db, sysDataList
    db = pymysql.connect(host="124.70.91.77", user="root", password="12345678", port=3306,
                         database='AnimeBigDataAnalysis')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    index = userId - 1000
    userData = sysDataList[index]
    # 动漫 anime
    aidList = list(userData[str(userId)][0].keys())  # [uid][1/2/3]
    for i in range(len(aidList)):
        a_markList = userData[str(userId)][0][aidList[i]]
        a_score = a_markList[0]
        a_ratio = a_markList[1]
        a_like = a_markList[2]
        a_collect = a_markList[3]
        a_timestamp = a_markList[4]
        sql1 = """INSERT INTO useranimehistory(uid, aid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (int(userId), int(aidList[i]), a_score, a_ratio, a_like, a_collect, a_timestamp)
        try:
            cursor.execute(sql1)
            # db.close()
            print({'message': 'anime successfully'})
        except:
            db.rollback()
            print({'message': 'anime fail'})
    db.commit()
    # 漫画 comic
    cidList = list(userData[str(userId)][1].keys())  # [uid][1/2/3]
    for i in range(len(cidList)):
        c_markList = userData[str(userId)][1][cidList[i]]
        c_score = c_markList[0]
        c_ratio = c_markList[1]
        c_like = c_markList[2]
        c_collect = c_markList[3]
        c_timestamp = c_markList[4]
        sql2 = """INSERT INTO usercomichistory(uid, cid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (int(userId), int(cidList[i]), c_score, c_ratio, c_like, c_collect, c_timestamp)
        try:
            cursor.execute(sql2)
            # db.commit()
            # db.close()
            print({'message': 'comic successfully'})
        except:
            db.rollback()
            print({'message': 'comic fail'})
    db.commit()
    # 小说 novel
    nidList = list(userData[str(userId)][2].keys())  # [uid][1/2/3]
    for i in range(len(nidList)):
        n_markList = userData[str(userId)][2][nidList[i]]
        n_score = n_markList[0]
        n_ratio = n_markList[1]
        n_like = n_markList[2]
        n_collect = n_markList[3]
        n_timestamp = n_markList[4]
        sql3 = """INSERT INTO usernovelhistory(uid, nid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (int(userId), int(nidList[i]), n_score, n_ratio, n_like, n_collect, n_timestamp)
        try:
            cursor.execute(sql3)
            # db.commit()
            # db.close()
            print({'message': 'novel successfully'})
        except:
            db.rollback()
            print({'message': 'novel fail'})
    db.commit()
    # cosplay
    cosidList = list(userData[str(userId)][3].keys())  # [uid][1/2/3]
    for i in range(len(cosidList)):
        cos_markList = userData[str(userId)][3][cosidList[i]]
        cos_score = cos_markList[0]
        cos_ratio = cos_markList[1]
        cos_like = cos_markList[2]
        cos_collect = cos_markList[3]
        cos_timestamp = cos_markList[4]
        sql4 = """INSERT INTO usercosplayhistory(uid, cosid, score, ratio, thumb, collect, time) VALUES (%d,%d,%d,%f,%d,%d,%d)""" \
               % (int(userId), int(cosidList[i]), cos_score, cos_ratio, cos_like, cos_collect, cos_timestamp)
        try:
            cursor.execute(sql4)
            db.commit()
            # db.close()
            print({'message': 'cosplay successfully'})
        except:
            db.rollback()
            print({'message': 'cosplay fail'})
    db.commit()





if __name__ == "__main__":
    jsonFile = open('..\\data_generation\\sysData.json', 'r')
    sysDataList = json.load(jsonFile)
    # print(sysDataList[1]['1001'][0].keys())
    for i in range(1000, 1300):
        print(insertUserJsonToDB(i))
    db.close()