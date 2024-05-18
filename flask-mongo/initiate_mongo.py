import json
from pymongo import MongoClient

# Connect to MongoDB running locally
client = MongoClient('mongodb://127.0.0.1', 27017)

# Access the 'test' database (create it if it doesn't exist); 'test' is the name of the DB, if your want another name, e.g., 'pspi', then replace 'test' with 'pspi'
print('creating and setting up db')
db = client['test']

# Load data from JSON file
print('loading data')
with open('catalog_example.json', 'r') as f:
    data = json.load(f)

print(data)

# you will add the data in a collection named 'test_col'; if your want another name, e.g., 'products', then replace 'test_col' with 'products' in the code below

# drop collection - optionally you can drop any existing collection; if you do not want it, then comment out the following 2 lines 
print('drop collection')
db.test_col.drop()

# Insert data into the 'test_col' collection
print('inserting data')
db.test_col.insert_many(data)

# create index for faster search with name; if you implement your search just by a field, then the following code is not needed; if you implemented with the 'search' method of MongoDB, then you need to have indexing
db.test_col.create_index([("name", "text")])

# Close the connection to MongoDB
print('closing connection')
client.close()
