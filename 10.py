#program returns external ip adress
import json
import urllib
data=json.load(urllib.urlopen('http://httpbin.org/get'))
print(data['origin'])
