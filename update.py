# Name: Group 8
# File: update.py
# Course: COP 3710
# Description: This file is intended to use DML to update information in the database
# ----------------------------------------------------------------------------------------------------------------------

# !/usr/bin/python

import sqlite3  # sql library


# update class
class Update:
    # create database connection
    def __init__(self, db):
        self.cur = None

        self.conn = sqlite3.connect(db)

        print("Opened database successfully")

    # update information to the internship table using DML
    def update(self, internship_id, internship_name, company, salary):
        self.cur.execute("UPDATE INTERNSHIP SET internship name = ?, company = ?, salary = ? WHERE ID = ?",
                         (internship_id, internship_name, company, salary))
        self.conn.commit()
        print("Total number of rows updated :", self.conn.total_changes)

        cursor = self.conn.execute("SELECT id, internship_name, company, salary from INTERNSHIP")
        for row in cursor:
            print("INTERNSHIP_ID = ", row[0])
            print("INTERNSHIP_NAME = ", row[1])
            print("COMPANY = ", row[2])
            print("SALARY = ", row[3], "\n")

        # close database
        print("Operation done successfully")
        self.conn.close()



