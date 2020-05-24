import requests
import json
url='http://admin:admin1234@172.26.132.189:5984/twitterdropbox2/'
headers={'Content-Type': 'application/json'}
i=0
with open("twitter-melb.json",encoding='utf-8',errors='ignore') as f:
        for line in f:
                line=line[:-2]
                if i!=0:
                        response=requests.post(url,data=line.encode('utf-8'),headers=headers)
                        #print(line)
                        print(response.status_code)
                        print(response.text)
                else:
                        i=i+1
print("completed")
print(i)
