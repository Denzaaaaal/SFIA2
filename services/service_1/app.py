from flask import Flask, render_template, request
import requests

app = Flask(__name__,template_folder="templates")

@app.route("/", methods = ['GET'])
def home():
    combined_name = requests.get("http://0.0.0.0:5003/joined_names")
    print(combined_name)
    full_name = combined_name.text
    return render_template("layout.html", full_name = full_name)

if __name__ == "__main__":
    app.run(port = 5000, host = "0.0.0.0", debug = True)