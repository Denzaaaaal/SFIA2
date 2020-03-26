from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/last_name", methods = ['GET'])
def last_name():
    list = ["Pollard","Bell", "Price", "Vance", "Mendez","Obrien", "Gould", "Lara", "Dennis", "Thomas", "Hurst", "Strickland"]
    return list[random.randrange(12)]

if __name__ == "__main__":
    app.run(port = 5002, host = "0.0.0.0", debug = True)