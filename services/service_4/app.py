from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/first_name", methods = ['GET'])
def first_name():
    """Pulls first name from service 2"""
    chosen_fname = requests.get("http://service_2:5001/first_name")
    chosen_first_name = chosen_fname.text
    print(chosen_first_name)
    return chosen_first_name

@app.route("/last_name", methods = ['GET'])
def last_name():
    """Pulls last name from service 3"""
    chosen_lname = requests.get("http://service_3:5002/last_name")
    chosen_last_name = chosen_lname.text
    print(chosen_last_name)
    return chosen_last_name
    
if __name__ == "__main__":
    app.run(port = 5003, host = "0.0.0.0", debug = True)