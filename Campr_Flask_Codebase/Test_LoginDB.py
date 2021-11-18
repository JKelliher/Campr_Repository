#!/usr/bin/env python3

import unittest
import Login_Credentials
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
    def test_InitialUser(self):
        conn = sqlite3.connect('LoginDB')
        c = conn.cursor()
        print("Initial check to see if mmartin is in the database")
        for row in c.execute("SELECT * FROM LoginCredentials;"):
            if row[1] == "mmartin":
                print("checking that mmartin is userID 1...")
                self.assertEqual(row[0], 1, "Error mmartin is not associated with userID 1")
                self.assertEqual(row[2], "mypassword", "Error mmartin not associated with the correct password")
                self.assertEqual(row[3], "mama4085@colorado.edu", "Error mmartin not associated with the correct email")
        print("InitialUser Test Passed!")
        print("\n")
        conn.commit()
        conn.close()
        pass

    #test to check addUser fuction
    def test_addUser(self):
        conn = sqlite3.connect('LoginDB')
        c = conn.cursor()

        #check that value error raised if no user name provided
        with self.assertRaises(ValueError):
            print("check that a ValueError is raised on null string for user name...")
            Login_Credentials.addUser("LoginDB", "", "mypassword", "mama4085@colorado.edu")

        #check that value error raised if invalid user name provided
        with self.assertRaises(ValueError):
            print("check that a ValueError raised if the user name is not a string...")
            Login_Credentials.addUser("LoginDB", 1, "mypassword", "mama4085@colorado.edu")

        #check that a value error raised if password is not long enough (needs to be at least 5 characters)
        with self.assertRaises(ValueError):
            print("check that a Value Error raised if password is not long enough...")
            Login_Credentials.addUser("LoginDB", "mmartin", "pass", "mama4085@colorado.edu")

        #check that a value error raised if no email provided
        with self.assertRaises(ValueError):
            print("check that a ValueError raised if no email provide...")
            Login_Credentials.addUser("LoginDB", "mmartin", "mypassword", "")

        #check that value error raised if non-valid email provided
        with self.assertRaises(ValueError):
            print("checking for a ValueError on non-valid email...")
            Login_Credentials.addUser("LoginDB", "mmartin", "mypassword", "mama4085")


        print("test_addUser passed!")
        conn.commit()
        conn.close()
        pass



# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

