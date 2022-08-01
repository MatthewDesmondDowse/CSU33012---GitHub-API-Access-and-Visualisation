# CSU33012-GitHub-API-Access-and-Visualisation
Repository for module CSU33012 to access data from the GitHub API and to take that data and visualize it in some way.

Code based on Professor Stephen Barrett's tutorial
https://bitbucket.org/esjmb/csu33012-python-github/src/master/

Started in Haskell, but now trying with Python.

In its current state, .sh files won't work from command line,
Code currently takes a users GitHub token from commandline,
Takes the data from GitHub and stores it in MongoDB via Docker,
Then code retrieves that information and creates a csv,
This csv is then graphed locally at http://localhost:8000/ using d3.
Still very basic and simple example from tutorial. 

Commands to run in command-line :

1) pip install github
2) pip install PyGitHub

For visualisation
1) more run-server.sh
2) python3 -m http.server 8000   (./run-server.sh won't work currently)
Name: http://localhost:8000

For Mongo Database
1)pip install pymongo

General Start
1) $cd to cloned repository
2) $docker-compose up
3) in a new shell cd to cloned repository again and $python3 script.py and paste token
4) $python3 script2.py
