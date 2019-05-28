# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:52:30 2019

@author: azumi
"""

import mysql.connector
 
# データベースへの接続とカーソルの生成

conn = mysql.connector.connect(
    host = '192.168.0.31',
    port = 3306,
    user = 'phpmyadmin',
    password = 'sz05ym8',
    database = 'python_db',
)

connected = conn.is_connected()
print(connected)
if (not connected):
    conn.ping(True)
    
