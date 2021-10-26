#!/usr/bin/env python3

import sqlite3
import sys
import os
import re

def create(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute("CREATE TABLE CampSites(idCamp INT, Site_Name VARCHAR, GPS VARCHAR, City VARCHAR, State VARCHAR, Date VARCHAR, Rating INT, Type VARCHAR, Restrooms VARCHAR, Fees VARCHAR, Notes VARCHAR);")
        conn.commit()
        conn.close()

def fill(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        Sites = [(1, 'Peaceful Valley', '40.13196, -105.50705', 'Allenspark', 'CO', '05/15/20', 4, 'Campground', 'Y', 'Y', 'Nice site, could hear street noise from peak to peak highway though'), \
                (2, 'Meeker Park', '40.24075, -105.53691', 'Allenspark', 'CO', '09/17/19', 3, 'Campground', 'Y', 'Y', 'Close to Longs Peak but otherwise not an exciting site'), \
                (3, 'Saddlehorn Campground', '39.10557, -108.73306', 'Grand Junction', 'CO', '06/2/20', 5, 'Campground', 'Y', 'Y', 'Nice spot close to Colorado National Monument but very little shade'), \
                (4, 'Behind the Rocks', '39.41833, -109.46079', 'Moab', 'UT', '11/12/20', 5, 'Dispersed', 'N', 'N', 'Lots of places to put down camp but in BLM land so no amenities and need a WAG bag'), \
                 (5, 'Masons Draw Campground', '38.54278, -109.30165', 'Moab', 'UT', '08/05/19', 5, 'Campground', 'Y', 'Y', 'In the trees near a great La Sal overlook'), \
                 (6, 'Rabbit Ears Pass', '40.36932, -106.68415', 'Steamboat Springs', 'CO', '06/25/21', 4, 'Dispersed', 'N', 'N', 'Great spot but high elevation so expect cooler nights and dispersed camping so no amenities'), \
                 (7, 'Dinosaur National Monument', '40.39770, -108.74606', 'Dinosaur', 'CO', '05/20/19', 3, 'Dispersed', 'N', 'N', 'The road in is a litte rough. 4x4 recommended but maybe not required. Near the Monument but otherwise, nothing special'), \
                 (8, 'North Alpine Loop', '43.19820, -111.04252', 'Alpine', 'WY', '08/10/21', 4, 'Campground', 'Y', 'Y', 'Great little campground near Alpine with a host and very clean restrooms. Most sites have some trees for seperation but you are still close to your neighbor.'), \
                 (9, 'Melvin BLM', '43.16567, -111.03739', 'Apline', 'WY', '08/13/21', 3, 'Dispersed', 'N', 'N', 'Basically in town but right across the way from Melvin brewing.'), \
                 (10, 'Camp City', '39.87203, -106.87816', 'Crested Butte', 'CO', '09/20/21', 4, 'Dispersed', 'N', 'N', 'Close to town and with a great view down a valley but it has a number of spots that are all relatively close to each other'), \
                 (11, 'Cement Creek', '38.82760, -106.83461', 'Crested Butte', 'CO', '09/20/19', 3, 'Campground', 'Y', 'Y', 'Close to town but no great views and sites are not great for a camper. Otherwise a nice spot in the trees for tent camping.')
                ]


        #insert into CampSites
        for (idcamp, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes) in Sites:
                c.execute("INSERT INTO CampSites VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (idcamp, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes))       
        conn.commit()
        conn.close()

        
def addCampsite(dbname, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    #check to see if campsite name was provided
    if site_name == "":
        print("Need to provide a site name")
        raise ValueError

    if type(site_name) != str:
        print("Site name needs to be a string")
        raise ValueError
        
    #check to see if GPS was provided
    if GPS == "":
        print("GPS required for site entry")
        raise ValueError
    

    #Check for GPS to be in correct format...
    if not bool(re.match("((?:[\+-]?[0-9]*[\.,][0-9]+)|(?:[\+-]?[0-9]+))", GPS)):
        print("GPS not in correct format. Please use decimal degrees format e.g. dd.dddddd, dd.ddddd")
        raise ValueError

    #check to see if a City was provided
    if City == "":
        print("Need to provide a city. Can be closest avialable")
        raise ValueError

    if type(City) != str:
        print("City name needs to be a string")
        raise ValueError
        
    #check to see if a state was provided
    if State == "":
        print("Need to provide a State.")
        raise ValueError

    #Check for all legal state abreviations    
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "RC", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if State not in states:
	print("Need to provide a valid state abbreviation. Abbreviation should be capitolized.")
	raise ValueError

    #Check to see if a date was provided
    if Date == "":
        print("Need to provide a date for visit to the camp site")
        raise ValueError

    #need a check to see if date in correct format mm/dd/yy
    if not bool(re.match("^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.]\d\d$", Date)):
        print("date not in the correct format. Please provide date in mm/dd/yy format.")
        raise ValueError
    
    #check to see if a rating was provided
    if Rating == "":
        print("Need to provide a rating for the site (0-5; where 0 is the worst and 5 is the best")
        raise ValueError
        
    if Rating < 0 or Rating > 5:
        print("Rating provided is out of range. Need to provide a rating for the site (0-5; where 0 is the worst and 5 is the best")
        raise ValueError

    #need a check for type
    
    #check for Restroom
    if Restroom != 'Y' and Restroom != 'N':
        print("Need to select Y (yes) or N (no) for restroom type")
        raise ValueError
    
    #check for Fees
    if Fees != 'Y' and Fees != 'N':
        print("Need to select Y (yes) or N (no) if fees are required for camping")
        raise ValueError
    
    idvalue = 0
    for row in c.execute("SELECT * FROM CampSites;"):
        idvalue = row[0]

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
    c.execute("INSERT INTO CampSites VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (newIdProd, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes))
    conn.commit()
    conn.close()

        
        
#def main():
#    create(sys.argv[1])
#    fill(sys.argv[1])

#hard coded for testing
def main():   
    create("CampTableDB")
    fill("CampTableDB")
    #addCampsite("CampTableDB", "newCamp", "40.04249, -105.02470", "Denver", "CO", "05/20/19", 5, "Campground", "Y", "N", "somenotes")
main()

