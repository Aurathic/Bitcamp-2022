# app.py
#from crypt import methods
from flask import Flask, render_template, request, jsonify, redirect, url_for
import recommend


app = Flask(__name__)

#creates dictionary with results, make webpage from that.
@app.route('/results', methods=['GET', 'POST'])
def results():
    
    user_dict = {'prices' : request.args.get('ret_price'), 
                'performance' : request.args.get('ret_prefo'), 
                'portability' : request.args.get('ret_port'), 
                'screen_quality' : request.args.get('ret_SQ')}
    

    return render_template('results.html')

#Index page.
@app.route('/') 
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
