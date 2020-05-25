from __future__ import absolute_import, print_function
import json
import re
import config
import couchdb
from urllib3.exceptions import ProtocolError
from tweepy import OAuthHandler, Stream, StreamListener
import requests


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=config.conumer_key
consumer_secret=config.consumer_secret

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=config.access_token
access_token_secret=confir.access_token_secret


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
        
    def on_data(self, data):
        #if there.search(data.text.lower()):
        language=["it","el","zh","ar","de"]
        data_json=json.loads(data)
        for id in db:
            if(db[id]["id"]==data_json["id"]):
                i=1
            else:
                i=0
        if(i==0):
            for i in language:
                if(data_json["lang"]== i):
                    save_file.write(data)
                    response=requests.post(url,data=data,headers=headers)

        return True
     

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    couch = couchdb.Server('https://admin:admin1234@172.26.129.166:5984/')
    db=['instance3_new']
    url='http://admin:admin1234@172.26.132.189:5984/instance3_new/'
    headers={'Content-Type': 'application/json'}
    save_file = open('Sydmelb_alllang.json','a')
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    location=[143.72314453125,-38.5825261593533,151.6552734375,-33.45894275368763]
    while True:
        try:
            stream.filter(locations=location)
        
        except (ProtocolError,AttributeError):
            print("Protocol error occurred, Restarting")
            continue  
    fhOut.close()
