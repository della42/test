from flask import Flask, render_template
from flask_json import json_response, FlaskJSON

import data

app = Flask(__name__)
FlaskJSON(app)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/table_data")
def table_data():
    return json_response(result = data.table_data)

if __name__ == '__main__':
   app.run(debug = True)
