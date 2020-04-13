from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import requests

app = Flask(__name__,template_folder="templates")
mysql = MySQL(app)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

@app.route("/", methods = ['GET'])
def home():
    combined_name = requests.get("http://service_4:5003/joined_names")
    full_name = combined_name.text
    if request.method == 'POST':
        status=request.form
        if 'create' in status:
            combined_name = requests.get("http://service_4:5003/joined_names")
            cur=mysql.connection.cursor()
            cur.execute('insert into name where full_name = %s', full_name)
        cur.close()
    return render_template("layout.html", full_name = full_name, title = "Name Generator")

if __name__ == "__main__":
    app.run(port = 5000, host = "0.0.0.0", debug = True)