# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import csv 
import sys
import random 
import re


with open("notebook_dataset.csv", "r") as f:
    reader = csv.DictReader(f)
    df = list(reader)
for row in df:
    row['performance'] = float(row['performance'])
    row['portability'] = float(row['portability'])
    row['screen_qual'] = float(row['screen_qual'])
    row['battery_qual'] = float(row['battery_qual'])
    row['Price_euros'] = float(row['Price_euros'])
websites = ["Newegg"] * 4 +  ["Amazon"]

print(df, file=sys.stderr)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/results', methods=['GET', 'POST'])
def results():
    #print(request.form, file=sys.stderr)
    price_min, price_max = list(map(int, request.form['price'].replace("$", "").split("-")))
    performance = float(request.form['performance'][:-1])
    portability = float(request.form['portability'][:-1])
    screen_quality = float(request.form['screen_quality'][:-1])
    battery_quality = float(request.form['battery_quality'][:-1])

    df_priced = list(filter(lambda row: price_min <= float(row['Price_euros']) and float(row['Price_euros']) <= price_max, df))

    overall_score = performance + portability + screen_quality + battery_quality
    df_priced = list(map(lambda row:
        row | {"score": 
            (performance * row['performance'] + 
            portability * row['portability'] + 
            screen_quality * row['screen_qual'] +
            battery_quality * row['battery_qual']) / 
            overall_score * 100,
            "website": random.choice(websites),
            "search_url": f"https://www.google.com/search?tbm=shop&q=" + 
                re.sub("\s", "+", re.sub("[^a-zA-Z0-9\s+]", "", row["Company"]+"+"+row["Product"]))
        },
        df_priced))

    df_priced.sort(key=lambda row: row["score"], reverse=True)
    print(f"{price_min} <= {df_priced[0]['Price_euros']} <= {price_max}", file=sys.stderr)
    return render_template('results.html', data=df_priced)

#Index page.
@app.route('/') 
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
