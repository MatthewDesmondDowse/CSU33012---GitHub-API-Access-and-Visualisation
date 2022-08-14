#this script accesses the GitHub API

#import Github from the PyGithub library
#from curses.ascii import isdigit
from datetime import datetime
from urllib import response
from urllib.request import urlopen
from github import Github   #GitHub API access
import json                 
import pymongo  
import requests
import re
import datetime
from faker import Faker
from collections import defaultdict
faker = Faker()
names = defaultdict(faker.name)

# ##insert token. Will need to change later to args
# # I have put "token" here to not leave any trace of personal tokens

token = input("Paste your token to continue ")

g = Github(token)

#Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

#Create a Database
db = client.classDB

#create list to store all contributors of d3 repo
contributors = []  
contributors_Url = f"https://api.github.com/repos/d3/d3/contributors"    
response = requests.get(contributors_Url)
data = response.json()

for repoC in data:
    contributors.insert(1,repoC["login"])

print(contributors , len(contributors))   

#Get creation date
d3_url = f"https://api.github.com/repos/d3/d3"
response = requests.get(d3_url)
data = response.json()

created_date = data["created_at"]
    
print(created_date)        






###-----------------------------------###    
# a = 1
# removechar='{"}:,'
# finalPercentages = []
  
# #gets URL for language breakdown in bytes   
# repoName = input("Enter name of repo to find language breakdown in bytes. ")
# url = "https://api.github.com/repos/{}/{}/languages".format(user.login, repoName)
# languages = requests.get(url).text

# #removes { } and : from json     
# for character in removechar:
#     languages=languages.replace(character,"")    
# print("JSON without { , } , and : " , languages)

# #seperate numbers(bytes) from data     
# bytesPerLanguage = re.findall(r'-?\d+', languages)  
# print("List of bytes" , bytesPerLanguage)

# #find total number of languages
# numOfLanguages = len(bytesPerLanguage)
# print("Number of languages = " , numOfLanguages)
    
# #find total number of bytes    
# totalBytes = sum(int(a) for a in re.findall(r'\d+', languages))
# print("Total Bytes = " , totalBytes)

# #find the percentage breakdown    
# for i in range(numOfLanguages):
#     x = bytesPerLanguage[i]
#     x = (int(x)/totalBytes) * 100
#     finalPercentages.insert(i,x)
#     print("Percentage breakdown is" ,x,"%") #prints a percentage
#     print(finalPercentages) #prints list of percentages

    
# listOfLanguages = re.findall(r'-?\D+', languages)
# print("List of languages: " , listOfLanguages)   
    
# dct = {'Repository name': repoName,
#        'Languages': listOfLanguages,
#        'Number of Languages' : numOfLanguages,
#        'Bytes_per_Language'  : bytesPerLanguage,
#        'List of percentages' : finalPercentages
#        }
# print("Dictionary is" + json.dumps(dct))

# db.githubuser.insert_many([dct])