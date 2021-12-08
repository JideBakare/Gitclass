print('hello world')
import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
serviceurl = "http://py4e-data.dr-chuck.net/json?"
sample_address = "South Federal University"
data_address = "Columbia University"
address_wanted = data_address

parameters = {"sensor": "false", "address": address_wanted}
paramsurl = urllib.parse.urlencode(parameters)

queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

data = urllib.request.urlopen(queryurl).read()


jsondata = json.loads(str(data))
place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
