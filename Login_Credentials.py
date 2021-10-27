import sqlite3
import sys
import os
import re

def create(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute("CREATE TABLE LoginCredentials(UserID INT, UserName VARCHAR, Password VARCHAR, Email VARCHAR);")
        conn.commit()
        conn.close()

def fill(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        Users = [(1, "mmartin", "mypassword", "mama4085@colorado.edu")
                ]


        #insert users into LoginCredentials
        for (UserID, UserName, Password, Email) in Users:
                c.execute("INSERT INTO LoginCredentials VALUES (?, ?, ?, ?);", (UserID, UserName, Password, Email))
        conn.commit()
        conn.close()


def addUser(dbname, user_name, password, email):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    idvalue = 0
    for row in c.execute("SELECT * FROM LoginCredentials;"):
        idvalue = row[0]

    if not bool(re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}$", email)):
        print("email not valid")
        raise ValueError

    newIdProd = idvalue + 1
    #print("newIDPROD: ", newIdProd)

    #CatID = -1
    #for row in c.execute("SELECT * FROM CampSites;"):
    #    if idCamp == row[0]:
    #        CatID = row[0]
    #    #else:
    #        #print("catID ValueError")
    #        #raise ValueError
    #if CatID == -1:
    #    print("CatID ValueError")
    #    raise ValueError

    #print("INPUT: ", newIdProd, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes)
    c.execute("INSERT INTO LoginCredentials VALUES(?, ?, ?, ?);", (newIdProd, user_name, password, email))
    conn.commit()
    conn.close()



#def main():
#    create(sys.argv[1])
#    fill(sys.argv[1])

#hard coded for testing
def main():
    create("LoginDB")
    fill("LoginDB")
    addUser("LoginDB", "User2", "User2Password", "somethign@colorado.edu")
main()
