#! /usr/bin/python

from flask import render_template
from flask import request
from app import app
import plivo

auth_id = "MAOTFKMGMWZMI5YME5OT"
auth_token = "MWI4NTA4ZDVhYmNmMjNlYzI5MTViMzlhZmQwNDFk"

p = plivo.RestAPI(auth_id, auth_token)   
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET'])
def index():

    dialNumber = request.args.get('dialNumber', '')
    # Make Calls
    params = {
    'from': '1212121212', # Caller Id
    'to' : dialNumber, # User Number to Call	
    'answer_url' : "http://talk-to-stranger.herokuapp.com/static/dial.xml",
    'answer_method' : 'GET'
    }
    response = p.make_call(params)

    print dialNumber, response

    return render_template('index.html', dialNumber=dialNumber)





