import urllib.request as ur
import urllib.parse as up

import json

serviceurl = "http://python-data.dr-chuck.net/json?"
address=input("enter location....")

url = serviceurl + up.urlencode({'address':address,'key':42})

print ('Retrieving:',url)

open_url=ur.urlopen(url)
data = open_url.read().decode()
print ('Retrived',len(data),'characters')

js=json.loads(str(data))

placeid = js['results'][0]['place_id']
print ("Place id:",placeid)
