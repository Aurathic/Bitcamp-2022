# app.py
#from crypt import methods
from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import sys

df = pd.read_csv("notebook_dataset.csv")
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#creates dictionary with results, make webpage from that.
@app.route('/results', methods=['GET', 'POST'])
def results():
    print(request.form, file=sys.stderr)
    price_min, price_max = list(map(int, request.form['price'].replace("$", "").split("-")))
    performance = float(request.form['performance'][:-1])/100
    portability = float(request.form['portability'][:-1])/100
    screen_quality = float(request.form['screen_quality'][:-1])/100

    df['score'] = df.apply(lambda row:
        performance * row['performance'] + 
        portability * row['portability'] + 
        screen_quality * row['screen_qual']
    , axis=1)

    df.sort_values(by="score", ascending=False, inplace=True)

    return render_template('results.html', data=df.to_dict())

#Index page.
@app.route('/') 
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
