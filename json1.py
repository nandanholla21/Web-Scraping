# http://py4e-data.dr-chuck.net/comments_1622081.json is the url
import json
from operator import index
from urllib.request import urlopen

url = input("Enter the url: ")
res= urlopen(url)
obj = json.loads(res.read())
formated_json = json.dumps(obj,indent=4)  # formatted_json only gives a string not an object
#print(formated_json)       
s=0
for item in obj["comments"]:
    s+=item["count"]
print(s)