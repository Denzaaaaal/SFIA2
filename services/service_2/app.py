from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/first_name", methods = ['GET'])
def first_name():
    list = ["Valeria","Perla", "Elisabeth", "Joanna", "Jordan","Violet", "Conor", "Whitney", "Ethen", "Ronan", "Selina", "Simone"]
    return list[random.randrange(12)]

if __name__ == "__main__":
    app.run(port = 5001, host = "0.0.0.0", debug = True)