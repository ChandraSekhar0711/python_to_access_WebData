import urllib
import json

input_url=input("http://py4e-data.dr-chuck.net/comments_507966.json")
open_url=urllib.urlopen(url)
data=open_url.read()

print(data)

comments=json.loads(str(data))
print("user_count:",len(comments))
sum1=0
for item in comments['comments']:
        x=item['count']
        sum1=sum1+x
print(sum1)
