# ============================================
# Title:  ross-user-service.py
# Author: Dan Ross
# Date:   11 December 2020
# Description: Exercise 9.2 – Querying and Creating Documents
# ===========================================

# imports

from pymongo import MongoClient

import pprint

import datetime

# connect to Mongo
client = MongoClient('localhost', 27017)

# use db web335
db = client.web335

# new user document
user = {
    "first_name": "Ned",
    "last_name": "Ryerson",
    "email": "needlenosened@gmail.com",
    "employee_id": "1234567",
    "date_created": datetime.datetime.utcnow()
}

# insert new user document
user_id = db.users.insert_one(user).inserted_id

# Output auto-generated user id
print(user_id)

# query the users collection to find newly added user and print results
pprint.pprint(db.users.find_one({"employee_id": "1234567"}))
