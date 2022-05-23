# Name: Group 8
# File: insert.py
# Course: COP 3710
# Description: This file is intended to use DML to  insert information into the databse
# ----------------------------------------------------------------------------------------------------------------------


# !/usr/bin/python

import sqlite3  # sql library


# create class to insert information
class Insert:
    # establish a sql connection
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)
        print("Opened database successfully")

    # DML insert statement
    def insert(self, internship_name, company, salary, internship_id):
        self.cur.execute("INSERT INTO INTERNSHIP (INTERNSHIP_ID,INTERNSHIP_NAME,COMPANY,ADDRESS, "
                         "PHONE_NUM, START_DATE, END_DATE) \
      VALUES (?, ?, ?, NULL)", (internship_name, company, salary, internship_id))
        # commit information
        self.conn.commit()
        # close database with inserted information
        print("Records created successfully")
        self.conn.close()


