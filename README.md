# CSU33012-GitHub-API-Access-and-Visualisation
Repository for module CSU33012 to access data from the GitHub API and to take that data and visualize it in some way.

Started in Haskell, but now trying with Python.

Commands to run in command-line :

1) pip install github
2) pip install PyGitHub

For visualisation
1) more run-server.sh
2) python3 -m http.server 8000   (./run-server.sh won't work currently)

For Mongo Database
1)pip install pymongo

General Start
1) cd to cloned repository
2) docker-compose up
3) python3 script.py and paste token
4) python3 script2.py
