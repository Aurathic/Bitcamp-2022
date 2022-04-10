# app.py
from crypt import methods
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# MAIN WEBPAGE
# API KEYS HERE. ADAM'S GOT THE ALGORITHM

#creates dictionary with results, make webpage from that.
@app.route('/results', methods=['GET', 'POST'])
def results():
    '''
    data = {}
    data["Price"] = request.form["price"]
    data["Performance"] = request.form["performance"]
    data["Portability"] = request.form["portability"]
    data["Screen Quality"] = request.form["screenquality"]
    '''
    data = {}

    return render_template('results.html')

#Index page.
@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    data = {}
    #data["Price"] = request.form["price"]
    data["Performance"] = request.form["performance"]
    data["Portability"] = request.form["portability"]
    data["Screen Quality"] = request.form["screenquality"]
    return data

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)