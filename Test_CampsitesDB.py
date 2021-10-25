#!/usr/bin/env python3

import unittest
import CampsiteDB
import sqlite3
import os

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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

    def test_addCampsite(self):
        conn = sqlite3.connect('CampTableDB')
        c = conn.cursor()

        #addProduct(dbName, site_name, GPS, City, State, Date, Rating, Type, Restroom, Fees, Notes)
        #good example: addProduct("CampTableDB", "Fremont Lake Campground", "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")

        with self.assertRaises(ValueError):
            print("check that a ValueError is raised on null string for Campsite name...")
            CampsiteDB.addCampsite("CampTableDB", "", "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking for a ValueError on non-string name for the campsite...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking to see if a GPS was provided...")
            CampsiteDB.addCampsite("CampTableDB", "Fremont Lake", "", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking a ValueError for an incorect format of GPS...")
            CampsiteDB.addCampsite("CampTableDB", 5, "4", "Pinedale", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if City not added...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "", "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking for ValueError if city was not a string...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", 5, "WY", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if State not added...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")
        with self.assertRaises(ValueError):
            print("checking for a ValueError if wrong abbreviation for state provided...")
            CampsiteDB.addCampsite("CampTableDB", 5, "42.94218, -109.79739", "Pinedale", "ZW", "8/25/20", 5, "Campground", "Y", "Y", "Nice spot right on Fremont Lake and very close to Pinedale.")

        print("test_addProduct passed!")
        conn.commit()
        conn.close()
        pass


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
