#!/usr/bin/env python3

import sqlite3
import sys
import os
import re

def create(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute("CREATE TABLE users(username, password, region);")
        conn.commit()
        conn.close()

def fill(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        Users = [('jacob_unger', 'password_1', 'CO'), \
                ('joe_kelliher', 'password_2, WI'), \
                ('matt_martin', 'password_3', 'NV'), \
                ('kelsey_kosnick', 'password_4', 'NY')]


        #insert into users
        for (username, password, region) in Users:
                c.execute("INSERT INTO users VALUES (?, ?, ?);", (username, password, region))       
        conn.commit()
        conn.close()

        
def addUser(username, password, region):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    #check to see if campsite name was provided
    if username == "":
        print("Please Provide a valid username")
        raise ValueError

    if type(password) == "" or len(password) <= 4:
        print("password must be greater than 4 characters")
        raise ValueError
        
    #check to see if region was provided
    if region == "":
        print("Region specification required!")
        raise ValueError
    
    
    idvalue = 0
    for row in c.execute("SELECT * FROM CampSites;"):
        idvalue = row[0]

    newIdProd = idvalue + 1


    c.execute("INSERT INTO users VALUES (?, ?, ?);", (username, password, region)) 
    conn.commit()
    conn.close()

        
#hard coded for testing
def main():   
    create("UserDB")
    fill("UserBD")
    #addCampsite("CampTableDB", "newCamp", "40.04249, -105.02470", "Denver", "CO", "05/20/19", 5, "Campground", "Y", "N", "somenotes")
main()


#Would love to check for password valifity, i.e. satisfies certain requirments