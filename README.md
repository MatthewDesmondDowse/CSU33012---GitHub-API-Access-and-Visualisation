# CSU33012-GitHub-API-Access-and-Visualisation
Repository for module CSU33012 to access data from the GitHub API and to take that data and visualize it in some way.

Code based on Professor Stephen Barrett's tutorial
https://bitbucket.org/esjmb/csu33012-python-github/src/master/

Started in Haskell, but now trying with Python.

Updated title: Construct a software system to automate the generation of a pie charts showing the total lines of code contribution of all contributors to the GitHub repository “d3/d3”, divided by month over the lifetime of the project

Issues with API access exist in current state as d3 repo is large and API limit can be exceeded quite quickly. Work arounds for this can be acquring a smaller data set e.g in script.py setting for loops to smaller numbers or even to 1, or setting the URL query to "?per_page=30&page=1" this will limit the data to 30 per page on page 1. 
d3 repo has over 4,300 commits, 120 contributors (123 in total but possible deleted accounts, number found via function made to calulate total contributors), and was created on the 27th of September 2010.

Also currently no way of getting lines of code via GitHub API. Instead my aim is to get the total changes (Additions and deletions of code) per commit by a user in a given month.

In its current state, .sh files won't work from command line,

Code currently takes a users GitHub token from commandline,
Takes the data from GitHub and stores it in MongoDB via Docker,
Then code retrieves that information and creates a csv appropriate for specific visualisiation, in this case a pie chart,
This csv is then graphed locally at http://localhost:8000/ using d3.
Still very basic and simple example from tutorial. 

Commands to run in command-line :

1) pip install github
2) pip install PyGitHub
3) pip install pymongo (For Mongo Database)

For visualisation
1) more run-server.sh
2) python3 -m http.server 8000   (./run-server.sh won't work currently)
Name: http://localhost:8000

General Start
1) $cd to cloned repository
2) $docker-compose up
3) in a new shell cd to cloned repository again and $python3 script.py and paste token
4) $python3 script2.py
