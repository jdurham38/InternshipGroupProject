# Name: Group 8
# File: sqlite.py
# Course: COP 3710
# Description: This file is intended to create the database.
# ----------------------------------------------------------------------------------------------------------------------

# !/usr/bin/python

import sqlite3  # sql library


# Establish sql connection

def __init__(self, db):
    self.cur = None

    self.conn = sqlite3.connect(db)
