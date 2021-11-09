#Automated Test Cases \
**Use Case1: Validate starting DB has correct City/State pairs for entries** \
    Verify that the starting DB has the correct City/State pairs for known entries \
**Description** \
    Test the starting DB entries to ensure it was set up correctly \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py \
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
    user may need to remove the CampTableDB before performing subsequent tests. \
     \
     \
     \
     \
**Use Case2: Validate starting DB has correct Campsite names for entries** \
    Verify that the starting DB has the correct Campsite names at the expected campID \
**Description** \
    Test the starting DB entries to ensure it was set up correctly \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py \
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
    user may need to remove the CampTableDB before performing subsequent tests. \
    
    
**Use Case3: Validate addCampsite works as expected** \
    Verify that the the addCampsite function works as expected \
**Description** \
    Test the addCampsite function to ensure it adds a new campsite into the database correctly. This will verify that the ValueErrors present in the function check to ensure user input correct format \
**Pre-Conditions** \
    CampTableDB does not exist otherwise user will get an error that it already exits and test will not run. \
**Test Steps** \
    Navigate to the Campr_Repository \
    run 'python Test_CampsitesDB.py \
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
    user may need to remove the CampTableDB before performing subsequent tests. \
    
    
    
**Use Case4: Validate addUser works as expected** \
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
    user may need to remove the LoginDB before performing subsequent tests. \
    
    
**Use Case5: Validate starting DB has correct information in it for login credentials** \
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
    user may need to remove the LoginDB before performing subsequent tests. \
