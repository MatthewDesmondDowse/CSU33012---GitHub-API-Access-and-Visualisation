print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

# githubuser = db.githubuser.find() #X

# for user in githubuser: #X
#     pprint.pprint(user) #X
#     print()             #X    


# ## IF I wanted to ensure no null data is retrieved 
# ## KEY: X means comment this line out 

# for user in db.githubuser.find({'user': {'$exists': True}}):
#      pprint.pprint(user)
#      print()
     

# now that we have data we want to generate an output that works for a visualisation
# I'm going to generate a simple bar chart that shows a count of public repos of each
# user in the database. Note that this isn't a great example of a visualisation of
# inteeresting data, but it's good enough for the purpose of demonstrating how to
# complete the link between data gathering and data visualisation.

# First let's describe the data structure our visualisation needs. Look to index.html
# for the code that uses it.

# I've previously discussed the use of json data and i recommend generating and transmitting data in json format.
# However because this example is so simple, I'm goign to write the data set out in csv format
# It will look like this:
#           User, Repo Count
#           Ben,12
#           Bill,2
#           Jack,34
#           Jill 50


with open('data.csv', 'w') as f:
    f.write('User, and their Repository language breakdown\n')
    dct = db.githubuser.find()
    for user in dct:
        pprint.pprint(user)
        print() #prints a blank line?
        f.write('%s\n' % (user))
            