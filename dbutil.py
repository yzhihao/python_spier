# -*- coding: utf-8 -*-
__author__ = 'yzh'
import mysql.connector

class dbutil():
    def __init__(self):
        pass

    def getcon(self):
        conn = mysql.connector.connect(user='root', password='123456', database='zhihu_spider', use_unicode=True)
        cursor = conn.cursor()
        return conn,cursor


    def closecon(self,con,cursor):
        con.commit()
        cursor.close()
        con.close()
