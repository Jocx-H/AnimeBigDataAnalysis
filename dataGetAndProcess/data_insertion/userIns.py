# -*- coding = utf-8 -*-
# @Time : 2022/6/25 15:34
# @File : userIns.py
# @Author : derrick

import random
import pymysql

db = None
def ins_user(userId: int, uname: str):
    global db
    db = pymysql.connect(host="124.70.91.77", user="root", password="xxx", port=3306,
                         database='AnimeBigDataAnalysis')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    password = '123456'
    sql = """INSERT INTO user(uid, uname, password) values(%d, '%s', '%s')"""%(userId, uname, password)
    try:
        cursor.execute(sql)
        db.commit()
        # db.close()
        return {'message': 'insert user successfully'}
    except:
        db.rollback()
        return {'message': 'insert user fail'}


'''main'''
if __name__ == "__main__":
    familyNameString = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐"
    familyNameList = list(familyNameString)
    for i in range(1000, 1200):
        if i <=1200 and i % 40 == 0:
            print("new type start")
        if i in range(1000, 1040):    # 中二
            uname = '中二' + random.choice(familyNameList)
            ins_user(i, uname)
        elif i in range(1040, 1080):  # 现充
            uname = '现充' + random.choice(familyNameList)
            ins_user(i, uname)
        elif i in range(1080, 1120):  # 肥宅
            uname = '肥宅' + random.choice(familyNameList)
            ins_user(i, uname)
        elif i in range(1120, 1160):  # 志怪
            uname = '志怪' + random.choice(familyNameList)
            ins_user(i, uname)
        elif i in range(1160, 1200):  # 青春
            uname = '青春' + random.choice(familyNameList)
            ins_user(i, uname)
        # else:                           # 无特定画像
        #     uname = '平凡' + random.choice(familyNameList)
        #     ins_user(i, uname)
    print('generate completed!')
    # 勿忘关闭数据库
    db.close()
    print('db closed.')