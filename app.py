# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import csv 
import sys




with open("notebook_dataset.csv", "r") as f:
    reader = csv.DictReader(f)
    df = list(reader)
for row in df:
    row['performance'] = float(row['performance'])
    row['portability'] = float(row['portability'])
    row['screen_qual'] = float(row['screen_qual'])
    row['battery_qual'] = float(row['battery_qual'])
    row['Price_euros'] = float(row['Price_euros'])

print(df, file=sys.stderr)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/results', methods=['GET', 'POST'])
def results():
    #print(request.form, file=sys.stderr)
    price_min, price_max = list(map(int, request.form['price'].replace("$", "").split("-")))
    performance = float(request.form['performance'][:-1])/100
    portability = float(request.form['portability'][:-1])/100
    screen_quality = float(request.form['screen_quality'][:-1])/100

    df_priced = list(filter(lambda row: price_min <= float(row['Price_euros']) or float(row['Price_euros']) <= price_max, df))

    df_priced = list(map(lambda row:
        row | {"score": 
            performance *row['performance'] + 
            portability * row['portability'] + 
            screen_quality * row['screen_qual']}, 
        df_priced))

    df_priced.sort(key=lambda row: row["score"], reverse=True)
    return render_template('results.html', data=df_priced)

#Index page.
@app.route('/') 
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
