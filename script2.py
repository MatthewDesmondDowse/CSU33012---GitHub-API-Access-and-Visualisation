print("Demonstration python based mongodb access");


from asyncio.windows_events import NULL
from ntpath import join

import pymongo              # for mongodb access
import pprint               # for pretty printing db data
import csv

from itertools import zip_longest

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

# Get data from database,
# find a way of making dataset smaller by time, e.g by year and then month,
# in smaller data set ensure that a user's total commit cahnges are added together
# as they can contribute many times in a month

with open('data.csv', 'w') as f:
    
    dct = db.githubuser.find()

    for data in dct: 
        #temp = data['All_Commit_Info']
        #print(temp)  
        f.write(str(data['All_Commit_Info']))
     
with open('dog2.csv', 'w', newline="") as f:
    header = ['Commit_Dates']
    dct = db.githubuser.find()
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows([elt] for elt in data['Commit_Dates'])
        
with open('data3.csv', 'w', newline="") as f:
    header = ['Commit_Logins']
    dct = db.githubuser.find()
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows([elt] for elt in data['Commit_Logins'])   
          
with open('data4.csv', 'w', newline="") as f:
    header = ['Total_Changes_per_Commit']
    dct = db.githubuser.find()
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows([elt] for elt in data['Total_Changes_per_Commit'])   
        
        
#################################

#CAREFUL THIS CODE MAKES AN ARRAY OF LENGTH 1

# with open('data4.csv', 'w') as f:
    
#     dct = db.githubuser.find()

#     for data in dct: 
#         f.write(str(data['Total_Changes_per_Commit']))  
 
########################################
#OLD CODE FOR OLD IDEA

# with open('data.csv', 'w') as f:
    
#     dct = db.githubuser.find()
    
#     for user in dct: 
#         pprint.pprint(user)
    
#         line = user['Languages']
#         line2 = user['Bytes_per_Language']
        
#         # result = list(zip(line,line2))
#         # print(result)
#         # np.savetxt("data.csv",result, delimiter=" ", fmt ='% s')
        
#         data = [line, line2]
#         export_data = zip_longest(*data, fillvalue = '')
#         with open('data.csv', 'w', encoding="ISO-8859-1", newline='') as f:
#             write = csv.writer(f)
#             write.writerow(("Languages", "Bytes_per_Language"))
#             write.writerows(export_data)