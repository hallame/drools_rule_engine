'''
Our application will solve a fictional problem that can be formulated using the following conditions.
A company called XYZ manufactures two types of computers: Type 1 and Type 2. The type of computer is determined by its architecture.
XYZ computers can perform a number of functions. At the moment, four functions are defined: DDNS Server, DNS Server, Gateway, and Router.
Each computer undergoes a series of tests before release.
The tests performed on each computer depend on its type and function. At the moment, five tests have been identified: "Test 1", "Test 2", "Test 3", "Test 4" and "Test 5".
A test deadline is set for each computer being tested. All tests corresponding to this computer must be performed no later than the specified date. The date itself depends on the tests selected for each specific computer.
Most of the XYZ company's test execution process is automated using internal software that selects a specific set of tests and determines the test date based on the type and function of computers.
Rules

At the moment, test suites and their execution dates for specific types of computers are selected in accordance with the following business rules.
Tests 1, 2, and 3 should be performed on Type 1 computers.
Tests 4 and 5 should be performed on Type 2 computers that perform the function of DNS servers.
Tests 2 and 3 should be performed on Type 2 computers serving as DDNS servers.
Tests 3 and 4 should be performed on Type 2 computers that perform the gateway function.
Tests 1 and 3 must be performed on Type 2 computers that perform the router function.
If test 1 is among the tests selected for this computer, then testing must be performed no later than three days after the production date. This rule takes precedence over all subsequent rules for choosing the test date.
If there is test 2 among the tests selected for this computer, then testing must be performed no later than seven days after the production date. This rule takes precedence over all subsequent rules for choosing the test date.
If there is test 3 among the tests selected for this computer, then testing must be performed no later than 10 days after the production date. This rule takes precedence over all subsequent rules for choosing the test date.
If Test 4 is among the tests selected for this computer, then testing must be performed no later than 12 days after the production date. This rule takes precedence over all subsequent rules for choosing the test date.
If Test 5 is among the tests selected for this computer, then testing must be performed no later than 14 days after the production date.
'''
