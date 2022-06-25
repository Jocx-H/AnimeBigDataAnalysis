#!/anaconda3/python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: utils.py
# @Author: WILLOSCAR
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 6月 25, 2022
# ---
import pymysql


def database():
    dbconfig = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'renjunbin007311',
        'database': 'anime',
        'charset': 'utf8'
    }
    conn = pymysql.connect(**dbconfig)
    cursor = conn.cursor()
    return conn, cursor
