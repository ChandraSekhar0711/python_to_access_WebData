import urllib
import xml.etree.ElementTree as ET

input_url=input("http://py4e-data.dr-chuck.net/comments_42.xml")
open_url=urllib.urlopen(url)
data=open_url.read()

comments=ET.fromstring(data)
lst=comments.findall('comments/comment')
print('user_count:',len(lst))
l=[]
sum=0
for item in lst:
	x=item.find('count').text
	l.append(int(x))
for i in l:
        sum=sum+i
print(sum)

