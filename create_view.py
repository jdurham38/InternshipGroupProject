# Name: Group 8
# File: create_view.py
# Course: COP 3710
# Description: This file is intended to use DML to  create a student view to select only certain information
# ----------------------------------------------------------------------------------------------------------------------


# !/usr/bin/python
import sqlite3  # SQL library


# create class for views
class Views:
    # create database conncection
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)
        self.conn = sqlite3.connect('internship.db')
        # create db view for student
        self.conn.execute('''
        CREATE VIEW student_view as 
        SELECT * FROM INTERNSHIP ''')
        # close database and print information from view
        print(self.conn.execute("SELECT * FROM student_view").fetchall())
        self.conn.close()
