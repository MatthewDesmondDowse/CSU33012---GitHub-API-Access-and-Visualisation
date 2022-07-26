
import pymongo              # for mongodb access

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.delete_many({})

print("Database Successfully cleared")
