#use flask file structure
    #static
        #js
        #css
    #templates
        #index.html

from flask import Flask, session, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/ag_data")
def agdata():
    data_path = "raw_data/cleaned_agdata.json"
    with open(data_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/county_geo")
def county_geo():
    data_path = "raw_data/acres_countyLevelGeo.json"
    with open(data_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/state_geo")
def state_geo():
    data_path = "raw_data/acres_stateLevelGeo.json"
    with open(data_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/map")
def map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
