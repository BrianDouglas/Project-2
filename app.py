#use flask file structure
    #static
        #js
        #css
    #templates
        #index.html
import os
import requests

from flask import Flask, session, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(): ,

