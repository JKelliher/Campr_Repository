# Campr Project Milestone 3
Joseph Kelliher \
Matthew Martin \
Kelsey Kosnik \
Jacob Unger

# Testing

TMPORTANT: A Milestone3 branch was created to capture the state of the repository at time of submission. Copy this branch for testing outlined in this document.

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
1. Navigate to the home page. Add "/home" to the base url to get there if "Home" link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/home"
4. Select the "Home" link on the header. Verify link reloads home page "/home". 
5. Select the "About" link on the header. Verify link takes you to the about page of the web application "/about". 
6. Navigate back to "/home". 
7. Select the "Login" link on the header. Verify link loads the login page "/login". 
8. Navigate back to "/home".
9. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register".

Navigation bar from the about page:
1. Navigate to the about page. Add "/about" to the base url to get there if "About" link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/about"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/about"
6. Select the "About" link on the header. Verify link reloads the about page "/about". 
7. Select the "Login" link on the header. Verify link loads the login page "/login".
8. Navigate back to "/about". 
9. Select the "Register" link on the header. Verify link takes you to the new user registration page "/register".
   
Navigation bar from the about User Register Page:
1. Navigate to the user registration page. Add "/register" to the base url to get there if "Register" link on header does not work. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/register"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/register"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/register" 
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/register" 
10. Select the "Register" link on the header. Verify link reloads the new user registration page "/register".
 
Navigation bar from the Search Nearby Page:
1. Navigate to the Search Nearby Page. Add "/search" to the base url to get there. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/search"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/search"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/search"
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/search" 
10. Select the "Register" link on the header. Verify link loads the new user registration page "/register".

Navigation bar from the Search Result Page:
1. Navigate to the Search Result page. Add "/search_result" to the base url to get there. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/search_result"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/search_result"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/search_result" 
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/search_result" 
10. Select the "Register" link on the header. Verify link loads the new user registration page "/register".

Navigation bar from the Create New Campsite Page:
1. Navigate to the Create New Campsite. Add "/new_campsite" to the base url to get there. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/new_campsite"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/new_campsite"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/new_campsite"
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/new_campsite" 
10. Select the "Register" link on the header. Verify link loads the new user registration page "/register".

Navigation bar from the Profile Page:
1. Navigate to the profile page. Add "/profile" to the base url to get there. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/profile"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/profile"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/profile"
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/profile" 
10. Select the "Register" link on the header. Verify link loads the new user registration page "/register".

Navigation bar from the Edit Profile Page:
1. Navigate to the profile page. Add "/edit_profile" to the base url to get there. 
2. Select the CAMPr link on the header. Verify link loads the login page "/login"
3. Navigate back to "/edit_profileprofile"
4. Select the "Home" link on the header. Verify link loads home page "/home". 
5. Navigate back to "/edit_profileprofile"
6. Select the "About" link on the header. Verify link loads the about page "/about".
7. Navigate back to "/edit_profileprofile"
8. Select the "Login" link on the header. Verify link loads the login page "/login".
9. Navigate back to "/edit_profileprofile" 
10. Select the "Register" link on the header. Verify link loads the new user registration page "/register".

**Expected Results** \
Each of the following links on the header navagetes to the coresponding page while user is on any of the pages in the web application:
1. Campr navigates to "/login"
2. Home navigates to "/home"
3. About navigates to "/about"
4. Login navigates to "/login"
5. Register navigates to "/register"
    
**Actual Results** \
On Each of the following pages of the web application the links of the header linked to the correspoinding page listed in expected result above:
1. Login page (All 5 header elements linked to correct page)
2. Home page (All 5 header elements linked to correct page)
3. About page (All 5 header elements linked to correct page)
4. User Registration Page (All 5 header elements linked to correct page)
5. Search Nearby Page (All 5 header elements linked to correct page)
6. Search Results Page (All 5 header elements linked to correct page)
7. Create New Campsite Page (All 5 header elements linked to correct page)
8. Profile Page (All 5 header elements linked to correct page)
9. Edit Profile Page (All 5 header elements linked to correct page)

**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    N/A 
    
    
 ## Use Case 2: Verify web app footer navigation funcitons as expected.
Verify that built in footer links to the correct page will user is on each page. \
**Description** \
    This test will verify the footer for the web application navigates to the correct pages\
**Pre-Conditions** \
    Campr web application has been opened in local browser. See steps 1 thru 5 listed user the "User Acceptance Testing" header for details on opening the web application in you local browser. \
**Test Steps:** \
Footer Navigation from the login page:
1. Navigate to the login page. Application will be at the login by default upon opening. 
2. Select the "Login" link on the footer. Verify link reloads the login page. 
3. Select the "About" link on the footer. Verify link takes you to the about page of the web application "/about".
4. Navigate back to /login. 
5. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
6. Navigate back to /login. 
7. Select the "search" link on the footer. Verify link loads the search page "/search"
  
Footer Navigation from the home page:
1. Navigate to the home page. Add "/home" to the base url to get there if "Home" link on header does not work. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /home.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /home. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /home. 
8. Select the "search" link on the footer. Verify link loads the search page "/search"

Footer Navigation from the about page:
1. Navigate to the about page. Add "/about" to the base url to get there if "About" link on header does not work. 
2. Select the "Login" link on the footer. Verify link reloads the login page. 
3. Navigate back to /about.
4. Select the "About" link on the footer. Verify link reloads about page of the web application "/about".
5. Navigate back to /about. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /about. 
8. Select the "search" link on the footer. Verify link loads the search page "/search"
   
Footer Navigation bar from the User Register Page:
1. Navigate to the user registration page. Add "/register" to the base url to get there if "Register" link on header does not work. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /register.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /register. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /register. 
8. Select the "search" link on the footer. Verify link loads the search page "/search"
 
Footer Navigation bar from the Search Nearby Page:
1. Navigate to the Search Nearby Page. Add "/search" to the base url to get there. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /search.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /search. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /search. 
8. Select the "search" link on the footer. Verify link reloads the search page "/search".

Footer Navigation bar from the Search Result Page:
1. Navigate to the Search Result page. Add "/search_result" to the base url to get there. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /search_result.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /search_result. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /search_result. 
8. Select the "search" link on the footer. Verify link loads the search page "/search".

Footer Navigation bar from the Create New Campsite Page:
1. Navigate to the Create New Campsite. Add "/new_campsite" to the base url to get there. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to "/new_campsite".
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to "/new_campsite". 
6. Select the "New Campsite" link on the footer. Verify link reloads the Create New Campsite page "/new_campsite". 
7. Select the "search" link on the footer. Verify link loads the search page "/search".

Footer Navigation bar from the Profile Page:
1. Navigate to the profile page. Add "/profile" to the base url to get there. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /profile.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /profile. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /profile. 
8. Select the "search" link on the footer. Verify link loads the search page "/search".

Navigation bar from the Edit Profile Page:
1. Navigate to the profile page. Add "/edit_profile" to the base url to get there. 
2. Select the "Login" link on the footer. Verify link loads the login page "/login. 
3. Navigate back to /edit_profile.
4. Select the "About" link on the footer. Verify link loads the about page of the web application "/about".
5. Navigate back to /edit_profile. 
6. Select the "New Campsite" link on the footer. Verify link loads the Create New Campsite page "/new_campsite". 
7. Navigate back to /edit_profile. 
8. Select the "search" link on the footer. Verify link loads the search page "/search".

**Expected Results** \
Each of the following links on the footer navagetes to the coresponding page while user is on any of the pages in the web application:
1. Login navigates to "/login"
2. About navigates to "/about"
3. New Campsite navigates to "/new_campsite"
4. Search navigates to "/Search"
    
**Actual Results** \
On Each of the following pages of the web application the links of the footer linked to the correspoinding page listed in expected result above:
1. Login page (All 4 footer elements linked to correct page)
2. Home page (All 4 footer elements linked to correct page)
3. About page (All 4 footer elements linked to correct page)
4. User Registration Page (All 4 footer elements linked to correct page)
5. Search Nearby Page (All 4 footer elements linked to correct page)
6. Search Results Page (All 4 footer elements linked to correct page)
7. Create New Campsite Page (All 4 footer elements linked to correct page)
8. Profile Page (All 4 footer elements linked to correct page)
9. Edit Profile Page (All 4 footer elements linked to correct page)

**Status (Pass/Fail)** \
    Pass \
**Notes** \
    N/A \
**Post-Conditions** \
    N/A 

## Use Case 3: Create New Campsite Form Correctly Validates User input.
Verify that the user entry form on the Create New Campsite page properly validates user input \
**Description** \
    This test will very that the user entry form on the Create New Campsite properly validates user input. The form was build with input validators that match the database contraints. \
**Pre-Conditions** \
    Campr web application has been opened in local browser. See steps 1 thru 5 listed user the "User Acceptance Testing" header for details on opening the web application in you local browser. \
**Test Steps** 
1. Navigate to the Create New Campsite page. Add "/new_campsite" to the base url or user page links to get the new campsite page.
2. Select the "submit" button at the bottom of the form without entering text in the "Site Name:" field.
3. Verify User is prompted to fill out the "Site Name:" field.
4. Enter "Test Campsite" in the site name field.
5. Select the submit button at the bottom of the form.
6. Verify the user is prompted to fill out the "City:" field.
7. Enter "test city" for the city.
8. Select the submit button at the bottom of the form.
9. verify the user is prompted to fill out the "Type of campsite:" field.
10. Enter "test type" for type of campsite.
11. Select the submit button at the bottom of the form.
12. Verify the user is prompted to fill out the following fields: "GPS Coordinates", "Date of Visit", "Restrooms", and "Fees".
13. Enter test for GPS coordinates.
14. Verify the user is prompted to enter GPS coordinates in the following format "dd.dddd, dd.dddd"
15. Enter 11.1111, 22.2222 for the GPS coordinates
16. Select Sumbit
17. Verify the user is prompted to enter date of visit in the following format mm/dd/yy.
18. Enter "test" for the date.
19. Verify the user is prompted to enter date of visit in the following format mm/dd/yy.
20. Enter "09/20/21 for the year.
21. Select Submit
22. Verify user is prompted that the Fees and Restrooms fields are required.
23. Select "Yes" for both fees and restrooms.
24. Select "Submit"
25. Verify form successfully submitted.

**Expected Results** \
Form does not submit unless the following is true:
1. user input values for the following fields: Site Name, City, GPS Coordinates, Date of Visit, Type of Campsite, Restrooms, and Fees.
2. GPS coordinates are formated dd.dddd, dd.dddd where d is a numeric values
3. Date of visit is formated dd/dd/dd
4. Either yes or no radio button for Restrooms and Fees is selected
5. User is prompted to correct error 
   
**Actual Results** 
1. Form did not submit when input was not provided for fields: Site Name, City, State, GPS Coordinates, Date of Visit, Type of Campsite, Restrooms, and Fees.
2. User was prompted to that field was required for Site Name, City, Type of Campsite, Restrooms, and Fees when data was not provided. 
3. User was prompted when input into fields  GPS Coordinates and Date of Visit was not formated correctly. 
4. Form submitted when all required fields had correctly formated user entries. 
    
**Status (Pass/Fail)** \
    Pass \
**Notes** \
    Form submission does not currently send data to database. Submission loads temporary page. \
**Post-Conditions** \
    N/A 
