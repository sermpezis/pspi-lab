from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test"

# PyMongo connects to the MongoDB
# server running on port 27017 on localhost, to the database named pspi
mongo = PyMongo(app)


### search API endpoint // GET method
### e.g., test it at the url "http://localhost:5000/search1?name=Pavlos
@app.route("/search1")
def search1():
    name = request.args.get("name")

    #### implementation: find one document

    doc = mongo.db.test_col.find_one({"name": name})
    ## The line below does the same as the line above, using a different method, i.e., the 'search' method in MongoDB (see also the initiate_mongo.py script)
    # doc = mongo.db.test_col.find_one({"$text": {"$search": name}})

    if doc is None:
        return "Name does not exist"

    ## different options for responses
    
    ## Option 1: returns only the name of the document
    # return doc["name"]

    ## Option 2: returns all the fields of the document 
    # Note: if you tried "return doc", this would not work because the document includes the "_id" field of MongoDB which cannot be serialized as a json object; you need first to remove this from the dict you return
    del doc['_id']
    return jsonify(doc)


### search API endpoint // GET method
### e.g., test it at the url "http://localhost:5000/search2?name=Pavlos
@app.route("/search2")
def search2():
    name = request.args.get("name")

    #### implementation: find all documents 
    docs = mongo.db.test_col.find({"name": name})
    print(docs)
    res = []
    for doc in docs:
        res.append({k:v for k,v in doc.items() if k != '_id'})
    if len(res)==0:
        return "Name does not exist"
    return jsonify(res)


### search API endpoint // POST method
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/search3 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/search3", methods=["POST"])
def search3():
    new_person = request.json
    name = new_person["name"]

    doc = mongo.db.test_col.find_one({"$text": {"$search": f"\"{name}\""}})
    if doc is None:
        return "Name does not exist"

    return doc["name"]


if __name__ =="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)



