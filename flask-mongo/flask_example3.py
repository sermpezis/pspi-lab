from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test"

# PyMongo connects to the MongoDB
# server running on port 27017 on localhost, to the database named `test`
mongo = PyMongo(app)


### add to db API endpoint - just prints a message
### e.g. test it at the url "http://localhost:5000/add1
@app.route("/add1", methods=["GET"])
def add_to_db1():

    # do nothing
    return "My DB just says \"Hello\"!", 200


### add to db API endpoint // POST method - body parameter
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/add2 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/add2", methods=["POST"])
def add_to_db2():

    #insert in Mondo DB - body parameter
    new_person = request.json
    print(new_person)
    mongo.db.test_col.insert_one(new_person)
    return "Addition made"


### add to db API endpoint // GET method - params
### e.g. test it at the url "http://localhost:5000/add3?name=Pavlos&year=1987&gender=male&property=10"
@app.route("/add3", methods=["GET"])
def add_to_db3():

    # insert in Mondo DB - params
    new_person = {}
    new_person["name"] = request.args.get('name')
    new_person["property"] = float(request.args.get('property'))
    print(new_person)
    mongo.db.test_col.insert_one(new_person)
    return "Addition made"


### add to db API endpoint // POST method - checks first if document exists
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/add4 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/add4", methods=["POST"])
def add_to_db4():

    # find/insert - to add later
    new_person = request.json
    print(new_person)
    # the find One returns the first document that matches your query criteria or null
    exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    if exists is None:
        mongo.db.test_col.insert_one(new_person)
    else:
        return "The person exists"
    return "Addition made"


### add to db API endpoint // POST method - updates if exists
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/add5 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/add5", methods=["GET","POST"])
def add_to_db5():

    # update
    new_person = request.json
    print(new_person)
    exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    if exists is not None:
        mongo.db.test_col.update_one({"name": new_person["name"]}, {"$set": {"property": new_person["property"]}})
    else:
        return "The person does not exist"
    return "Updated"


### add to db API endpoint // POST method - deletes if exists
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/add6 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/add6", methods=["POST"])
def add_to_db6():

    # delete
    new_person = request.json
    exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    if exists is not None:
        # Removes a single document from a collection
        mongo.db.test_col.delete_one({"name": new_person["name"]})
    else:
        return "The person does not exist"
    return "Deleted"




if __name__ =="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)



