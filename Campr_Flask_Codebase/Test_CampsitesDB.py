#!/usr/bin/env python3

import unittest
import CampsiteDB
import sqlite3
import os

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        pass

    def tearDown(self):
        #if self.db.conn:
        #    self.db.conn.close()
        os.remove('test.db')
        pass

    #this is a test to spot check a couple city state pairs
    def test_CityState(self):
        conn = sqlite3.connect('CampTableDB')
        c = conn.cursor()
        print("Checking the database to see if cities are associated with the intended state")
        for row in c.execute("SELECT * FROM CampSites;"):
            if row[3] == "Allenspark":
                print("checking that Allenspark is in Colorado...")
                self.assertEqual(row[4], "CO", "Error Allenspark is not associated with CO")
            if row[3] == "Moab":
                print("checking that Moab is in UT...")
                self.assertEqual(row[4], "UT", "Error Moab is not associated with UT")
            if row[3] == "Alpine":
                print("Checking that Alpine is associated with WY...")
                self.assertEqual(row[4], "WY", "Error Alpine is not associated with WY")
        print("Test_CitySate Passed!")
        print("\n")
        conn.commit()
        conn.close()
        pass




    #This is a test to spot check that a couple of camps are associated with the correct state
    def test_CampsiteNames(self):
        conn = sqlite3.connect('CampTableDB')
        c = conn.cursor()
        print("Spot checking database that campsites are associated with the right state...")
        for row in c.execute("SELECT * FROM CampSites;"):
            if row[1] == "Meeker Park":
                print("checking Meeker Park is in CO...")
                self.assertEqual(row[4], "CO", "Error...Meeker Park not associated with CO")
            if row[1] == "North Alpine Loop":
                print("checking North Alpine Loop is in WY...")
                self.assertEqual(row[4], "WY", "Error... North Alpine Loop is not associated with WY")
            if row[1] == "Masons Draw Campground":
                print("checking Mason Draw Campgroun is in UT...")
                self.assertEqual(row[4], "UT", "Error... Masons Draw is not associated with UT")
        print("Test_CampsiteNames!")
        print("\n")
        conn.commit()
        conn.close()
        pass

    def test_addCampsite(self):
        conn = sqlite3.connect('CampTableDB')
        c = conn.cursor()

        #addProduct(dbName, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes)
        #good example: addProduct("CampTableDB", "Fremont Lake Campground", "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")

        with self.assertRaises(ValueError):
            print("check that a ValueError is raised on null string for Campsite name...")
            CampsiteDB.addCampsite("CampTableDB", "", "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking for a ValueError on non-string name for the campsite...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking to see if a GPS was provided...")
            CampsiteDB.addCampsite("CampTableDB", "Fremont Lake", "", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking a ValueError for an incorect format of GPS...")
            CampsiteDB.addCampsite("CampTableDB", 5, "4", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if City not added...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking for ValueError if city was not a string...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", 5, "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if State not added...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if wrong abbreviation for state provided...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "ZW", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.", "")

        print("test_addProduct passed!")
        conn.commit()
        conn.close()
        pass




# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

