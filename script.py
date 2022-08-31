# this script accesses the GitHub API

# import Github from the PyGithub library
#from curses.ascii import isdigit
#from datetime import datetime
from urllib import response
from urllib.request import urlopen
from github import Github  # GitHub API access
import pymongo
import requests
from faker import Faker
from collections import defaultdict
import numpy as np
import json

faker = Faker()
names = defaultdict(faker.name)

# ##insert token. Will need to change later to args
# # I have put "token" here to not leave any trace of personal tokens

token = input("Paste your token to continue ")
username = input("Paste your username to continue ")

g = Github(token)

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a Database
db = client.classDB

#####################################################################
# Get SHA COMMIT HISTORY
# From my own manual testing with URL queries I know there are
# 44 pages of commits when the page displays 100 commits per page
#4341 commits

# CHANGE TO PER_PAGE=30 FOR TESTING
#Update: this should remove any duplicate or unwanted SHAs from url

i = 1
x= 0
sha_list = []
commits_url = f"https://api.github.com/repos/d3/d3/commits?per_page=100&page="

while i <= 44:  # change to 44 later on, issues with api access
    url1 = commits_url+str(i)
    response = requests.get(url1, auth=(username, token))
    data4 = response.json()
    
    for x in range(len(data4)):
        sha_list.append(data4[x]['sha'])
        
    i = i + 1
    
#print(sha_list, len(sha_list))

###################################################################

# Take list of sha and search for each url with sha,
# take login name, date comitted, and number of changes made
# 4 lists, list 1 of everything in order or date, login, total changes,
# list 2 of just dates
# list 3 of just login names
# list 4 of just total changes
# there are over 4,300+ commits since 2010

commit_info = []
commit_info_url = "https://api.github.com/repos/d3/d3/commits"

commit_dates = []
commit_login = []
commit_total_changes = []
j = 0

while j < len(sha_list):
    temp_url = f"{commit_info_url}/{sha_list[j]}"
    response = requests.get(temp_url, auth=(username, token))
    data5 = response.json()
    
    #for k in range(3):
    commit_info.append(data5['commit']['author']['date'])
    commit_info.append(data5['commit']['author']['name'])
    commit_info.append(data5['stats']['total'])
    
    j = j + 1    

#print(commit_info)

#get list sorted by date
# N = 3
# fill = len(commit_info)
# tempList = commit_info + [fill] * N
# subList = [tempList[n:n+N] for n in range(0, len(commit_info), N)]

# subList.sort()

# output = []


# def removeNestings(l):
#     for i in l:
#         if type(i) == list:
#             removeNestings(i)
#         else:
#             output.append(i)


# removeNestings(subList)
# #print(output)

for i in range(0, len(commit_info), 3):
    commit_dates.append(commit_info[i])
    commit_login.append(commit_info[i+1])
    commit_total_changes.append(commit_info[i+2])

# print(commit_dates)
# print(commit_login)
# print(commit_total_changes)
####################################################################

# store info in a dictionary and then into database

dct = {'All_Commit_Info': commit_info,
       'Commit_Dates': commit_dates,
       'Commit_Logins': commit_login,
       'Total_Changes_per_Commit': commit_total_changes
       }

##print("Dictionary is" + json.dumps(dct))

db.githubuser.insert_many([dct])

#####################################################################

# SOME HELPER FUNCTIONS I MADE PREVIOUSLY, COULD BE USEFUL...

# create list to store all NAMES OF CONTRIBUTORS of d3 repo

# #CHANGE TO PER_PAGE=30 FOR TESTING
# contributors = []
# contributors_Url = f"https://api.github.com/repos/d3/d3/contributors?per_page=30"
# response = requests.get(contributors_Url)
# data = response.json()

# for repoC in data:
#     contributors.insert(0,repoC["login"])

# # #GitHub only shows 100 contributors per page so we have to go to second page
# # #we know d3 has 123 contributors from GitHub,
# # #This counts 120, possible deleted accounts

# # #CHANGE TO PER_PAGE=30 FOR TESTING
# # contributors_Url_page2 =f"https://api.github.com/repos/d3/d3/contributors?page=2&per_page=30"
# # response = requests.get(contributors_Url_page2)
# # data2 = response.json()

# # for repoC in data2:
# #     contributors.insert(0,repoC["login"])

# print(contributors , len(contributors))

######################################################################
# #Get CREATION DATE
# d3_url = f"https://api.github.com/repos/d3/d3"
# response = requests.get(d3_url)
# data3 = response.json()

# created_date = data3["created_at"]

# print(created_date)


##############################################################################################################

###-----------OLD CODE FOR OLD IDEA---------------------###
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
