#use flask file structure
    #static
        #js
        #css
    #templates
        #index.html

from flask import Flask, session, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
