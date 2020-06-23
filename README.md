# supportgenie
Exercise 2
Agent selector
You are given the following data for agents 
agent
is_available
available_since (the time since the agent is available)
roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Please write a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  

```
## Files Present 
---sales.py
---inputgenerator.py
---sales_testcase.py
---testcase.txt
```
## Input Format 

First Line Contains Number of Agents (n)/
Second Line Contains Number of Queries(q)/
n Line with Agent Details [name is_available available_for roles]/
q Line with Query Detail [roles method(1,2,3)]/
/
## Sample Input
4/
4/
LOFV True 25 Python,Sales/
GJYQ True 13 Tech,Sales,English/
MJRQ False 18 Tech/
WQLE True 24 Tech,Spanish,Sales/
Tech 1/
Tech,Sales,English 1/
Tech,Sales,English 3/
Tech,Spanish,Sales 3/

### Note
Method 1 - All Available/
Method 2 - Least Busy/
Method 3 - Random/
## How to run the code
Use sales.py for manual entry of test case. Please only use the format given above/
To generate test case use inputgenerator.py. This program will prompt for input for number of agents and number of queries. The output will be stored to testcase.txt, you can manually change the file but again please only use the format mentioned above./
To use the testcase stored in testcase.txt use sales_testcase.py/

## Sample Output
All suitable agents are busy right now for query Tech/
Query for Tech,Sales,English : Using Method 1(All Available Agents)/
Assigning Query to Agent GJYQ/
Query for Tech,Sales,English : Using Method 3(Random Assign)/
Assigning Query to Agent GJYQ/
Query for Tech,Spanish,Sales : Using Method 3(Random Assign)/
Assigning Query to Agent WQLE/
