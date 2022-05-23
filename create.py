# Name: Group 8
# File: create.py
# Course: COP 3710
# Description: This file is intended to use DML to  create tables into the database
# ----------------------------------------------------------------------------------------------------------------------


# !/usr/bin/python
import sqlite3  # sql library


# create table class
class Tables:
    # create database connection
    def __init__(self, db):

        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        # Create student table
        self.conn.execute('''CREATE TABLE STUDENT (ID INT PRIMARY KEY     NOT NULL, 
        NAME           TEXT    NOT NULL, 
        EMAIL          CHAR(30)     NOT NULL, 
        PASSWORD       CHAR(12) NOT NULL CHECK ([PASSWORD] like '%[0-9]%' AND [
        PASSWORD] like '%[A-Z]%' AND [PASSWORD] like '%[!@#$%^&*()-_+=.,;:~]%' AND length([
        PASSWORD])>=(8)), 
        ADDRESS        CHAR(50), 
        PHONE_NUM      INT CHECK (length(PHONE_NUM >= 10)));''')

        # Create internship table
        self.conn.execute('''CREATE TABLE INTERNSHIP
            (INTERNSHIP_ID INT PRIMARY KEY     NOT NULL,
            INTERNSHIP_NAME           TEXT    NOT NULL,
            REMOTE        BOOL,
            SALARY         INT,
            START_DATE     DATE,
            END_DATE       DATE,
            FOREIGN KEY(INTERNSHIP_NAME) REFERENCES COMPANY(EMPLOYER_ID)
            );''')

        # Create company table
        self.conn.execute('''CREATE TABLE COMPANY
        (EMPLOYER_ID INT PRIMARY KEY NOT NULL,
        COMPANY_ID INT NOT NULL,
        EMPLOYER_NAME TEXT,
        COMPANY_NAME TEXT,
        FOREIGN KEY(COMPANY_ID) REFERENCES INTERNSHIP(INTERNSHIP_ID)
        ''')

        # Create admin table
        self.conn.execute(''' CREATE TABLE ADMIN
            (ADMIN_ID INT PRIMARY KEY NOT NULL,
            ADMIN_NAME TEXT,
            COMPANY_EXT INT,
            COMPANY_LOCATION CHAR (50));''')

        # commit and close database
        print("Table created successfully")
        self.conn.commit()
        self.conn.close()
