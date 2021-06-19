import pymysql

conn=pymysql.connect(
host= 'localhost',
database= 'test',
user= 'root',
password= '',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor
)

cursor=conn.cursor()
sql_query=""" CREATE TABLE book(
id integer PRIMARY KEY,
author text NOT NULL,
language text NOT NULL,
title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()