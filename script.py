#this script accesses the GitHub API

from github import Github

##insert token. Will need to change later to args
# I have put "token" here to not leave any trace of personal tokens
g = Github("token") 

user = g.get_user()
print("user: " + user.login)
