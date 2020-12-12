# ============================================
# Title:  ross-user-update.py
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

# update a user's email address
db.users.update_one(
    {"employee_id": "1234567"},
    {
        "$set": {
            "email": "dawross@my365.bellevue.edu"
        }
    }
)

# query the users collection to find newly updated user and print results with email, employee id, first name, and last name.
pprint.pprint(db.users.find_one({"employee_id": "1234567"},{"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))
