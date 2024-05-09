from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test"

# PyMongo connects to the MongoDB
# server running on port 27017 on localhost, to the database named pspi
mongo = PyMongo(app)


### add to db API endpoint // POST method
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/add -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
@app.route("/add", methods=["GET","POST"])
def add_to_db():

    # do nothing
    return "My DB just says \"Hello\"!", 200

    # #insert in Mondo DB - body parameter
    # new_person = request.json
    # print(new_person)
    # mongo.db.test_col.insert_one(new_person)
    # return "Addition made"

    # # insert in Mondo DB - params
    # new_person = {}
    # new_person["name"] = request.args.get('name')
    # new_person["property"] = float(request.args.get('property'))
    # print(new_person)
    # mongo.db.test_col.insert_one(new_person)
    # return "Addition made"


    # # find/insert - to add later
    # new_person = request.json
    # print(new_person)
    # # the find One returns the first document that matches your query criteria or null
    # exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    # if exists is None:
    #     mongo.db.test_col.insert_one(new_person)
    # else:
    #     return "The person exists"
    # return "Addition made"


    # # update
    # new_person = request.json
    # print(new_person)
    # exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    # if exists is not None:
    #     mongo.db.test_col.update_one({"name": new_person["name"]}, {"$set": {"property": new_person["property"]}})
    # else:
    #     return "The person does not exist"
    # return "Updated"


    # # delete
    # new_person = request.json
    # exists = mongo.db.test_col.find_one({"name": new_person["name"]})
    # if exists is not None:
    #     # Removes a single document from a collection
    #     mongo.db.test_col.delete_one({"name": new_person["name"]})
    # else:
    #     return "The person does not exist"
    # return "Deleted"




if __name__ =="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)



