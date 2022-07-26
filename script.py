#this script accesses the GitHub API

#import Github from the PyGithub library
from github import Github

##insert token. Will need to change later to args
# I have put "token" here to not leave any trace of personal tokens
g = Github("token") 

user = g.get_user()

print("user: " + user.login)

#will now work if location field is empty on GitHub profile
if user.location is not None:
     print("location: " + user.location)


