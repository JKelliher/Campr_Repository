# Campr Project Milestone 3
Joseph Kelliher \
Matthew Martin \
Kelsey Kosnik \
Jacob Unger

# Testing
Note: The following are packages required to run testing of this project: \
Python3 \
Sqlite3 \
Flask \
Flask-WTForms \
SQLAlchemy


# Automated Test Cases 
To run the automated test cases ensure python 3 and sqlite3 are installed. Navigate to the Campr_Repository. \
Ensure file CampTableDB.db does not exist in the folder. \
Run Test_cCampsitesDB.py using python3 to execute the automated tests. \
The purpose and output of each test are detailed below:

## Use Case 1: Validate starting DB has correct City/State pairs for entries
Verify that the starting DB has the correct City/State pairs for known entries \
**Description** \
    Test the starting DB entries to ensure it was set up correctly \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py' \
**Expected Results** \
    you should see the following text and pass one of the tests \
    >".Checking the database to see if cities are associated with the intended state \
    >checking that Allenspark is in Colorado... \
    >checking that Allenspark is in Colorado... \
    >checking that Moab is in UT... \
    >checking that Moab is in UT... \
    >Checking that Alpine is associated with WY... \
    >Test_CitySate Passed!" \
**Actual Results** \
    >".Checking the database to see if cities are associated with the intended state \
    >checking that Allenspark is in Colorado... \
    >checking that Allenspark is in Colorado... \
    >checking that Moab is in UT... \
    >checking that Moab is in UT... \
    >Checking that Alpine is associated with WY... \
    >Test_CitySate Passed!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    user may need to remove the CampTableDB before performing subsequent tests. 

## Use Case 2: Validate starting DB has correct Campsite names for entries 
Verify that the starting DB has the correct Campsite names at the expected campID \
**Description** \
    Test the starting DB entries to ensure it was set up correctly \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py' \
**Expected Results** \
    you should see the following text and pass one of the tests \
    >"Spot checking database that campsites are associated with the right state... \
    >checking Meeker Park is in CO... \
    >checking Mason Draw Campgroun is in UT... \
    >checking North Alpine Loop is in WY... \
    >Test_CampsiteNames!" \
**Actual Results** \
    >"Spot checking database that campsites are associated with the right state... \
    >checking Meeker Park is in CO... \
    >checking Mason Draw Campgroun is in UT... \
    >checking North Alpine Loop is in WY... \
    >Test_CampsiteNames!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    user may need to remove the CampTableDB before performing subsequent tests.
    
    
    
## Use Case 3: Validate addCampsite works as expected
Verify that the the addCampsite function works as expected \
**Description** \
    Test the addCampsite function to ensure it adds a new campsite into the database correctly. This will verify that the ValueErrors present in the function check to ensure user input correct format \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py' \
**Expected Results** \
    you should see the following text and pass one of the tests \
    >".check that a ValueError is raised on null string for Campsite name... \
    >Need to provide a site name \
    >checking for a ValueError on non-string name for the campsite... \
    >Site name needs to be a string \
    >checking to see if a GPS was provided... \
    >GPS required for site entry \
    >checking a ValueError for an incorect format of GPS... \
    >Site name needs to be a string \
    >checking for a ValueError if City not added... \
    >Site name needs to be a string \
    >checking for ValueError if city was not a string... \
    >Site name needs to be a string \
    >checking for a ValueError if State not added... \
    >Site name needs to be a string \
    >checking for a ValueError if wrong abbreviation for state provided... \
    >Site name needs to be a string \
    >test_addProduct passed!" \
**Actual Results** \
    >".check that a ValueError is raised on null string for Campsite name... \
    >Need to provide a site name \
    >checking for a ValueError on non-string name for the campsite... \
    >Site name needs to be a string \
    >checking to see if a GPS was provided... \
    >GPS required for site entry \
    >checking a ValueError for an incorect format of GPS... \
    >Site name needs to be a string \
    >checking for a ValueError if City not added... \
    >Site name needs to be a string \
    >checking for ValueError if city was not a string... \
    >Site name needs to be a string \
    >checking for a ValueError if State not added... \
    >Site name needs to be a string \
    >checking for a ValueError if wrong abbreviation for state provided... \
    >Site name needs to be a string \
    >test_addProduct passed!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    user may need to remove the CampTableDB before performing subsequent tests.
    
    
    
## Use Case 4: Validate addUser works as expected
Verify that the the addUser function works as expected to the LoginDB \
**Description** \
    Test the addUser function to ensure it adds a new user into the database correctly. This will verify that the ValueErrors present in the function check to ensure user input correct format \
**Pre-Conditions** \
    LoginDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_LoginDB.py \
**Expected Results** \
    you should see the following text and pass one of the tests \
    >".check that a ValueError is raised on null string for user name... \
    >user name required \
    >check that a ValueError raised if the user name is not a string... \
    >user name must be a string \
    >check that a Value Error raised if password is not long enough... \
    >password must be at least 5 characters long \
    >check that a ValueError raised if no email provide... \
    >must provide an email \
    >checking for a ValueError on non-valid email... \
    >email not valid \
    >test_addUser passed!" \
**Actual Results** \
    >".check that a ValueError is raised on null string for user name... \
    >user name required \
    >check that a ValueError raised if the user name is not a string... \
    >user name must be a string \
    >check that a Value Error raised if password is not long enough... \
    >password must be at least 5 characters long \
    >check that a ValueError raised if no email provide... \
    >must provide an email \
    >checking for a ValueError on non-valid email... \
    >email not valid \
    >test_addUser passed!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    user may need to remove the LoginDB before performing subsequent tests.
    
    
## Use Case 5: Validate starting DB has correct information in it for login credentials
Verify that the starting DB has the correct content for known entries \
**Description** \
    Test the starting DB entries to ensure it was set up correctly \
**Pre-Conditions** \
    LoginDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_LoginDB.py \
**Expected Results** \
    you should see the following text and pass one of the tests \
    >"Initial check to see if mmartin is in the database \
    >checking that mmartin is userID 1... \
    >InitialUser Test Passed!" \
**Actual Results** \
    >"Initial check to see if mmartin is in the database \
    >checking that mmartin is userID 1... \
    >InitialUser Test Passed!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    user may need to remove the LoginDB before performing subsequent tests.
    
    
# User Acceptance Testing
To run the automated test cases ensure the following are installed: \
Python3 \
Sqlite3 \
Flask \
Flask-WTForms \
Perform the following to open the web application:
1. After Clonging the repository open the command terminal. 
2. From the command line Navigate to the Campr_Repository directory. 
3. Navigate to Campr_Flask_Codebase directory.
4. Run campr_app.py using python 3. 
5. open the URL for the web application. It should be displayed with text similar to "Running on http://127.0.1:5000/ (Press CTRL+C to quit)"
\
\
See below for each user test case:

## Use Case 1: Verify web app header navigation funcitons as expected.
Verify that built in header links to the correct page will user is on each page. \
**Description** \
    This test will verify the header for the web application navigates to the correct pages\
**Pre-Conditions** \
    Campr web application has been opened in local browser. See steps 1 thru 5 listed user the "User Acceptance Testing" header for details on opening the web application in you local browser. \
**Test Steps:** \
Navigation bar from the login page:
1. Navigate to the login page. Application will be at the login by default upon opening. 
2. Select the CAMPr link on the header. Verify link reloads the login page "/login"
3. Select the "Home" link on the header. Verify link takes you to the home page of the web application "/home". 
4. Navigate back to /login. 
5. Select the "About" link on the header. Verify link takes you to the about page of the web application "/about". 
6. Navigate back to /login. 
7. Select the "Login" link on the header. Verify link reloads the login page. 
8. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register". 
  
Navigation bar from the home page:
1. Navigate to the home page. Add "/home" to the base url to get there if home link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/home"
4. Select the "Home" link on the header. Verify link reloads home page "/home". 
5. Select the "About" link on the header. Verify link takes you to the about page of the web application "/about". 
6. Navigate back to "/home". 
7. Select the "Login" link on the header. Verify link loads the login page "/login". 
8. Navigate back to "/home".
9. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register".

Navigation bar from the about page:
1. Navigate to the about page. Add "/about" to the base url to get there if home link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/about"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/about"
6. Select the "About" link on the header. Verify link reloads the about page "/about". 
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/about". 
10. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register".
   
Navigation bar from the about Register Page:
1. Navigate to the about page. Add "/about" to the base url to get there if home link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/about"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/about"
6. Select the "About" link on the header. Verify link reloads the about page "/about". 
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/about". 
10. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register".
 
**Expected Results** \
    you should see the following text and pass one of the tests \
    >".Checking the database to see if cities are associated with the intended state \
    >checking that Allenspark is in Colorado... \
    >checking that Allenspark is in Colorado... \
    >checking that Moab is in UT... \
    >checking that Moab is in UT... \
    >Checking that Alpine is associated with WY... \
    >Test_CitySate Passed!" \
**Actual Results** \
    >".Checking the database to see if cities are associated with the intended state \
    >checking that Allenspark is in Colorado... \
    >checking that Allenspark is in Colorado... \
    >checking that Moab is in UT... \
    >checking that Moab is in UT... \
    >Checking that Alpine is associated with WY... \
    >Test_CitySate Passed!" \
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    N/A \
