#alice_blue
import alice_blue
from alice_blue import *

#threading
import threading

#time.sleep()
import time


class socket:

    #global variables
    live_data=[]
    socket_opened = False
    
    #credentials
    username='242661'
    password='&Khyati0'
    #api_secret='AYBTHY25UFEDJ6EZY6ZISK1K0LBEUX18XGKB038P8RJF2660WHAZNWP07025XXL6'
    #app_id='UNOFFICED'
    twoFA='khyati'
    

    


    #alice.start_websocket handlers
    def _event_handler_quote_update(self,message):
        self.live_data.append(message)

    def _open_callback(self):
        self.socket_opened = True


    #init.py
    def __init__(self,app_id,api_secret):

        self.app_id=app_id
        self.api_secret=api_secret


        #access token and alice objects
        self.access_token = AliceBlue.login_and_get_access_token(username=self.username, password=self.password, twoFA=self.twoFA, api_secret=self.api_secret, app_id=self.app_id)

        self.alice = AliceBlue(username=self.username, password=self.password, access_token=self.access_token, master_contracts_to_download=['NSE', 'BSE'])

        
        self.alice.start_websocket(subscribe_callback=self._event_handler_quote_update,
                            socket_open_callback=self._open_callback,
                            run_in_background=True)
        
        while (self.socket_opened==False):
            pass


            

    #subscription methods

    def subscribe_nse_market(self,instruments):
        for x in instruments :
            self.alice.subscribe(self.alice.get_instrument_by_symbol('NSE', x), LiveFeedType.MARKET_DATA)

    def subscribe_nse_snapquote(self,instruments):
        for x in instruments :
            self.alice.subscribe(self.alice.get_instrument_by_symbol('NSE', x), LiveFeedType.SNAPQUOTE)

    def subscribe_bse_market(self,instruments):
        for x in instruments :
            self.alice.subscribe(self.alice.get_instrument_by_symbol('BSE', x), LiveFeedType.MARKET_DATA)

    def subscribe_bse_snapquote(self,instruments):
        for x in instruments :
            self.alice.subscribe(self.alice.get_instrument_by_symbol('BSE', x), LiveFeedType.SNAPQUOTE)
            

            


 



