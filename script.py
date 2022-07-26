#this script accesses the GitHub API

#import Github from the PyGithub library
from github import Github   #GitHub API access
import json                 
import pymongo  

##insert token. Will need to change later to args
# I have put "token" here to not leave any trace of personal tokens
token = input("Paste your token to continue ")
g = Github(token) 

user = g.get_user()

# print("user: " + user.login)

# #will now work if location field is empty on GitHub profile
# if user.location is not None:
#      print("location: " + user.location)

dct = { 'user': user.login, 'location': user.location}

print ("dictionary is " + json.dumps(dct))


#Storing dictionary into a Mongo Database

#Remove null fields
for k, v in dict(dct).items():
    if v is None:
        del dct[k]
        
print("Cleaned dictionary is " + json.dumps(dct))

#Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

#Create a Database
db = client.classDB

db.githubuser.insert_many([dct])

                

