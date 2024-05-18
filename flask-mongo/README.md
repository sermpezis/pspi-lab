# Πληροφορικά Συστήματα Παγκοσμίου Ιστού - Lab: APIs, Flask, Mongo, Crawlers

***

## Web crawlers with Python's library selenium

For ubuntu (linux) you need to have  Chrome installed. 

E.g., You can see how to do it here: https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian

or, quicker (what worked for me on my Ubuntu 22.04 system, but may not work directly):  
- `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
- `dpkg -i google-chrome-stable_current_amd64.deb`
- `pip3 install webdriver-manager`


#### Step 1: Import necessary libraries

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
```

#### Step 2: define your options and url for scraping 
e.g., 
```python
url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"
options = Options()
options.headless = True # does not apper as window

```


#### Step 4: create your driver (i.e., the agent that will do the scraping/crawling)

**For windows**
```python
driver = webdriver.Chrome(options=options)
```

**For Linux (Ubuntu)**
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
```


#### Step 5: do the parsing / crawling

See a few examples:
-  [crawler_example.py](./crawler_example.py)
-  [crawler_example1.py](./crawler_example1.py)
-  [crawler_example2.py](./crawler_example2.py)



***

## Setup a MongoDB

#### Step 1: start the MongoDB server

See instructions in course material / slides.

E.g., for Linux:
- Start the mongo server with `sudo systemctl start mongod`
- Check the status with `sudo systemctl status mongod`

or, with Docker
- Start mongo with docker `docker run -d -p 27017:27017 --name mongodb mongo`


#### Step 2: Create a database

E.g., see an example on how to do it with Python in the file [initiate_mongo.py](./initiate_mongo.py)

```bash
python initiate_mongo.py
```

this script connects to the MongoDB (at the location `mongodb://127.0.0.1:27017`) and creates a DB and collection, and inputs the data from the file [catalog_example.json](./catalog_example.json)



***

## Create a Web API with Python's Flask framework


#### Setup your environment and run flask

Steps: 

1. create virtual envinorment and activate it; e.g., in Ubuntu
	- `python -m venv venv`
    - `source ./venv/bin/activate`

2. install requirements (when the virtual env is activated): `pip install -r requirements.txt`

3. run flask application; some options for how to do it
    - A) add the `app.run(...)` in the end of your script, e.g., see example [flask_example1.py](flask_example1.py) and then type in the terminal `python flask_example1.py`
    - B) run directly from the terminal, e.g., `flask --app flask_example1.py run --debugger`

Notes:

- you will get interactive feedback in the terminal when an error occurs during a request
- in option A, when you change your code the API is updated automatically (you don't neet to kill the python script and restart it)



#### Example 1: the simplest simplest implementation of an API

In [flask_example1.py](flask_example1.py) there is a simplest simplest implementation of an API that returns only a text

How to test it: e.g., Go to your browser and visit the url `localhost:5000/` and the reponse of the API should appear in your browser




#### Example 2: search endpoint 

In [flask_example2.py](flask_example2.py) there is an API with three endpoints with which you can search documents in the DB:
- `/search1`: returns one document with the given name; e.g., `http://localhost:5000/search1?name=Pavlos`
- `/search2`: returns all documents with the given name; e.g., `http://localhost:5000/search2?name=Pavlos`
- `/search3`: (implementation with POST method) returns one document with the name of the given json data; e.g., `curl -X POST -H "Content-Type: application/json" http://localhost:5000/search3 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'`





#### Example 3: add endpoint 

In [flask_example3.py](flask_example3.py) there is an API with 6 endpoints that add/update/delete entries in the DB:
- `/add1`: just prints a message; e.g., `"http://localhost:5000/add1`
- `/add2`: adds a document in the DB; POST method - body parameter; e.g., `curl -X POST -H "Content-Type: application/json" http://localhost:5000/add2 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'`
- `/add3`: adds a document in the DB; GET method - params; e.g., `http://localhost:5000/add3?name=Pavlos&year=1987&gender=male&property=10`
- `/add4`: adds a document in the DB; POST method - checks first if document exists; e.g., `curl -X POST -H "Content-Type: application/json" http://localhost:5000/add4 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'`
- `/add5`: updates a document in the DB; POST method - updates if exists; e.g., `curl -X POST -H "Content-Type: application/json" http://localhost:5000/add5 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'`
- `/add6`: deletes a document in the DB; POST method - deletes if exists; e.g., `curl -X POST -H "Content-Type: application/json" http://localhost:5000/add6 -d '{"name":"Pavlos","year":1987,"gender":"male","property":10.0}'`