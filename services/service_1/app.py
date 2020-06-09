from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import requests, os

app = Flask(__name__,template_folder="templates")
mysql = MySQL(app)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        # Creating name
        generated_first_name = requests.get("http://service_4:5003/first_name")
        generated_last_name = requests.get("http://service_4:5003/last_name")
        first_name = generated_first_name.text
        last_name = generated_last_name.text
        cur = mysql.connection.cursor()
        cur.execute('insert into names(first_name, last_name) values (%s, %s)', (first_name, last_name))
        cur.execute('select * from names')
        rows = cur.fetchall()
        names = []

        for row in rows: 
            names.append(row)

        mysql.connection.commit()
        cur.close() 
        return render_template("layout.html", first_name = first_name, last_name = last_name, title = "Name Generator", names = names)
    return render_template("instructions.html", title = "Name Generator")

if __name__ == "__main__":
    app.run(port = 5000, host = "0.0.0.0", debug = True)