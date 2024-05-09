from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test"

# PyMongo connects to the MongoDB
# server running on port 27017 on localhost, to the database named pspi
mongo = PyMongo(app)


### search API endpoint // GET method
@app.route("/search")
def search():
    name = request.args.get("name")

    #### implementation: find one

    # doc = mongo.db.test_col.find_one({"name": name})
    doc = mongo.db.test_col.find_one({"$text": {"$search": f"\"{name}\""}})
    if doc is None:
        return "Name does not exist"

    # return doc["name"]
    # return doc # this does not work
    # print(doc)
    del doc['_id']
    return jsonify(doc)


    #### implementation: find all
    
    # docs = mongo.db.test_col.find({"name": name})
    # print(docs)
    # res = []
    # for doc in docs:
    #     res.append({k:v for k,v in doc.items() if k != '_id'})
    # if len(res)==0:
    #     return "Name does not exist"
    # return jsonify(res)






### search API endpoint // POST method
### e.g. curl -X POST -H "Content-Type: application/json" http://localhost:5000/search -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'
# @app.route("/search", methods=["POST"])
# def search():
#     new_person = request.json
#     name = new_person["name"]

#     doc = mongo.db.test_col.find_one({"$text": {"$search": f"\"{name}\""}})
#     if doc is None:
#         return "Name does not exist"

#     return doc["name"]


if __name__ =="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)



