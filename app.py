

#sub sripts
import alice_obj, data_process, upload

#file acess
import os

#time.sleep
import time

#time stamps
import datetime
from datetime import timedelta


#FLASK APP
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return work_logs

work_logs='fail'

def run_it():
    
    #start time (IST)
    start_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).isoformat()
    

    #instruments_list
    nse_instruments, bse_instruments = data_process.instruments_list()
    
    
    
    #sockets and quote_types variables
    nse_sockets=[]
    bse_sockets=[]
    nse_quote_type=['nse-m', 'nse-m', 'nse-m', 'nse-m', 'nse-m', 'nse-m', 'nse-s', 'nse-s', 'nse-s', 'nse-s', 'nse-s', 'nse-s',]
    bse_quote_type=['bse-m', 'bse-m', 'bse-m', 'bse-m', 'bse-m', 'bse-m', 'bse-s', 'bse-s', 'bse-s', 'bse-s', 'bse-s', 'bse-s',]

    #socket object creation
    for i in range(0,12):
        nse_sockets.append(alice_obj.socket(nse_quote_type[i]))
        bse_sockets.append(alice_obj.socket(bse_quote_type[i]))

    #subscription
    for i in range(0,12):
        j=i
        i=i%6 #instruments are shared between market and snapquote sockets
        if (i+1)*250 > len(nse_instruments) or (i+1)*250 > len(bse_instruments) :
            nse_sockets[j].subscribe(nse_instruments[250*i:len(nse_instruments)])
            bse_sockets[j].subscribe(bse_instruments[250*i:len(bse_instruments)])

        else:
            nse_sockets[j].subscribe(nse_instruments[250*i:250*(i+1)])
            bse_sockets[j].subscribe(bse_instruments[250*i:250*(i+1)])



    
    
    #sleep for data collection; As of now it'll be 10 mins
    time.sleep(5)
    
    
    #data_clean ( exchange variable for file_name)
    nse_file_name=data_process.data_clean(nse_sockets, 'nse')
    bse_file_name=data_process.data_clean(bse_sockets, 'bse')
    
    
    #upload
    upload.upload(nse_file_name)
    upload.upload(bse_file_name)

    #delete those files after upload
    os.remove(nse_file_name)
    os.remove(bse_file_name)
    
    #endtime (IST)
    end_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).isoformat()

    #work_logs to be returned to flask's @app.route('/') 
    work_logs = '  (IST)  ' + 'start : ' + start_time + ' end : ' + end_time
    return work_logs

work_logs=run_it()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)