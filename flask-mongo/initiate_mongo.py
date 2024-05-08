import json
from pymongo import MongoClient, TEXT

# Connect to MongoDB running locally
client = MongoClient('mongodb://127.0.0.1', 27017)

# Access the 'pspi' database (create it if it doesn't exist)
print('creating and setting up db')
db = client['test']

# Load data from JSON file
print('loading data')
with open('catalog_example.json', 'r') as f:
    data = json.load(f)

print(data)

# drop collection
print('drop collection')
db.test_col.drop()

# Insert data into the 'my_col' collection
print('inserting data')
db.test_col.insert_many(data)

# create index for faster search with name
db.test_col.create_index([("name", TEXT)])

# Close the connection to MongoDB
print('closing connection')
client.close()
