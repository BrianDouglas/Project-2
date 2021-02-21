#use flask file structure
    #static
        #js
        #css
    #templates
        #index.html

from flask import Flask, session, request, render_template, jsonify
import json
import pymongo
from py_scripts import bd_config

bd_config.init()

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

@app.route("/api/<state>")
def state_api(state):
    #make connection
    connectTo = "ag_data"
    client = pymongo.MongoClient(f"mongodb+srv://{bd_config.USERNAME}:{bd_config.PASSWORD}@bricluster.yskth.mongodb.net/{connectTo}?retryWrites=true&w=majority")
    #nav to collection
    db = client.ag_data
    records = db.ag_records
    #process incoming
    state = state.upper()
    #run query
    result = records.find({'state': state}, {"_id": False})
    result = list(result)
    #check for no results
    if len(result) == 0:
        return jsonify({"ERROR": "STATE does not exist in database, sorry."}), 404
    #return results
    return jsonify(result)

@app.route("/api/<state>/<county>")
def county_api(state, county):
    #make connection
    connectTo = "ag_data"
    client = pymongo.MongoClient(f"mongodb+srv://{bd_config.USERNAME}:{bd_config.PASSWORD}@bricluster.yskth.mongodb.net/{connectTo}?retryWrites=true&w=majority")
    #nav to collection
    db = client.ag_data
    records = db.ag_records
    #process incoming
    state = state.upper()
    county = county.upper()
    #run query
    result = records.find({'state': state,'county': county}, {"_id": False})
    result = list(result)
    #check for no results
    if len(result) == 0:
        return jsonify({"ERROR": "STATE/COUNTY combo does not exist in database, sorry."}), 404
    #return results
    return jsonify(result)

if __name__ == "__main__":

    app.run(debug=True)
