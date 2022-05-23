# Name: Group 8
# File: Select.py
# Course: COP 3710
# Description: This file is intended to use DML to select information from the database
# ----------------------------------------------------------------------------------------------------------------------

# !/usr/bin/python

import sqlite3  # sql database


# create select class
class Select:
    # create database connection
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)
        print("Opened database successfully")

    # define a fetch in order to receive information using DML
    def fetch(self, internship_name=''):
        self.cur.execute(
            "SELECT * FROM INTERNSHIP WHERE INTERNSHIP_NAME LIKE ?", ('%' + internship_name + '%',))
        rows = self.cur.fetchall()
        return rows

    # define another fetch to gather all information in the database
    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

        # close connection

    print("Operation done successfully")




