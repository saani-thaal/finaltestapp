"""
HIDDEN JUST FOR TEST 



#file_path :  quant/first5min/draft

import alice_obj

from flask import Flask

import pickle, time
import pandas as pd
import multiprocessing

with open('instruments.pickle', 'rb') as f:
    ins=pickle.load(f)
    
ins1=ins[:250]
ins2=ins[250:]

app_id1='CetEoSQctj'
api_secret1='sGWyHQ7B0PneyCkQ38No7CPKSpJdFkN1uzghvvdD976Pcvju8B9KdPznQKe6GHP5'

app_id2='TdGD3kas16'
api_secret2='5d2rOQcqH4R4SGAY5DZ5OL1iYSqU5q7g1lyfYXWyzsNwUPtrw9R1y02omY9RYaN7'


def market():
    global ins1
    a=alice_obj.socket(app_id1,api_secret1)
    a.subscribe_nse_market(ins1)
    time.sleep(5)
    pd.DataFrame(a.live_data[:]).to_csv('market.csv')
    print('market')


def snapquote():
    global ins2
    b=alice_obj.socket(app_id1,api_secret1)
    b.subscribe_nse_snapquote(ins2)
    time.sleep(5)
    pd.DataFrame(b.live_data[:]).to_csv('snapquote.csv')
    print('snap')


app = Flask(__name__)
appp= Flask(__name__)


@app.route("/")
def hello():
    market()
    return "market"

@appp.route("/")
def hi():
    snapquote()
    return "snapquote"


def a():
    global app
    app.run(host='0.0.0.0', port=8080)
    
def b():
    global appp
    appp.run()



if (__name__ == "__main__"):
    
    p1 = multiprocessing.Process(target=a)
    p2 = multiprocessing.Process(target=b)

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
    
   HIDDEN JUST FOR TEST
   """

from flask import Flask
@app.route("/")
def hello():
    return "vasanth akka"

app = Flask(__name__)

if (__name__ == "__main__"):
    app.run()
