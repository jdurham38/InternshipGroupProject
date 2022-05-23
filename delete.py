# Name: Group 8
# File: delete.py
# Course: COP 3710
# Description: This file is intended to use DML to delete information from the database
# ----------------------------------------------------------------------------------------------------------------------


# !/usr/bin/python

import sqlite3  # sql library


# delete class
class Delete:
    # create connection
    def __init__(self, db):
        self.cur = None
        self.conn = sqlite3.connect(db)

    # delete internships using internship ID
    def remove(self, internship_id):
        self.conn.execute("DELETE from INTERNSHIP where ID = ?;", (internship_id,))
        self.conn.commit()
        print("Total number of rows deleted :", self.conn.total_changes)

        # close connection
        print("Operation done successfully")
        self.conn.close()


def db():
    return None


