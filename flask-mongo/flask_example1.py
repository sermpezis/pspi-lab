from flask import Flask, jsonify, request
'''
Steps: 
1) create virtual envinorment and activate it; e.g., in Ubuntu
    python -m venv venv
    source ./venv/bin/activate

2) install requirements: pip install -r requirements.txt

3) run flask application; some options for how to do it
    A) add the app.run(...) in the end of your script (see below), and then type in the terminal "python flask_example1.py"
    B) run directly from the terminal "flask --app flask_example1.py run --debugger"

# flask - -app main run - -debugger --> terminal --> Activating a connection via Flask with interactive
# feedback from the browser when an error occurs during a request
'''

############################################################################################
# Setting Flask

# According to the official flask documentation, a __name__ argument
# is passed in the Flask class to create its instance,
# which is then used to run the application
app = Flask(__name__)

###########################################################################

# API calls


# API call 1 - get request
@app.route("/")
def api_call_1():
    return jsonify({"res": "This is our first API Call"})
    # return "This is our second API call"




if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)