from __future__ import absolute_import, print_function
import json
import re
from urllib3.exceptions import ProtocolError
from tweepy import OAuthHandler, Stream, StreamListener
import requests


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="9le5bnTxSTGud2N6HhIJBqyZz"
consumer_secret="ZSaumIGqIgdzHlEuj8mZKfrUtDPj61RVAgxmfR4r6RYyJqeuTl"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1253249603547172869-EH1hqkIydJkoodnV28uUhG0tbm01Kb"
access_token_secret="ViwDAGTVKu5UEyRGIDs0LRy1kal0YB0sVGaWy6vRHfGEQ"


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
        
    def on_data(self, data):
        #if there.search(data.text.lower()):
        language=["it","el","zh","ar","de"]
        data_json=json.loads(data)
        for i in language:
            if(data_json["lang"]== i):
               save_file.write(data)
               response=requests.post(url,data=data,headers=headers)

        return True
     

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
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
