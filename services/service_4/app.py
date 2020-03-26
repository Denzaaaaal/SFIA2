from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/joined_names", methods = ['GET'])
def full_name():
    chosen_fname = requests.get("http://0.0.0.0:5001/first_name")
    chosen_lname = requests.get("http://0.0.0.0:5002/last_name")
    combined_name = chosen_fname.text + " " + chosen_lname.text
    print(combined_name)
    return combined_name

if __name__ == "__main__":
    app.run(port = 5003, host = "0.0.0.0", debug = True)