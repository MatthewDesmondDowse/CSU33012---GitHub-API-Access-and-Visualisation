print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

githubuser = db.githubuser.find() #X

for user in githubuser: #X
    pprint.pprint(user) #X
    print()             #X    


## IF I wanted to ensure no null data is retrieved 
## KEY: X means comment this line out 

# for user in db.githubuser.find({'location': {'$exists': True}}):
#      pprint.pprint(user)
#      print()