print("Demonstration python based mongodb access");


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



with open('data.csv', 'w') as f:
    
    dct = db.githubuser.find()
    
    for user in dct: 
        pprint.pprint(user)
    
        line = user['Languages']
        line2 = user['Bytes_per_Language']
        
        # result = list(zip(line,line2))
        # print(result)
        # np.savetxt("data.csv",result, delimiter=" ", fmt ='% s')
        
        data = [line, line2]
        export_data = zip_longest(*data, fillvalue = '')
        with open('data.csv', 'w', encoding="ISO-8859-1", newline='') as f:
            write = csv.writer(f)
            write.writerow(("Languages", "Bytes_per_Language"))
            write.writerows(export_data)