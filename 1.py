#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests
city="北京"
payload = {"city": city}
headers = {'content-type': 'application/json'}
r = requests.get('http://www.sojson.com/open/api/weather/json.shtml',params=payload,headers=headers)
print type(r)
print r.status_code
print r.encoding
print r.cookies
print r.text
#print r.json()