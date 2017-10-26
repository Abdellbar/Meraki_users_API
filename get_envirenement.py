import requests
import browsercookie
import json
from urlparse import urlparse
import sys

url_base = "alternavelly put your link here"
if sys.argv[1]:
    url_base=sys.argv[1]

parrsed_url = urlparse(url_base)
#get browser cookies 
cj = browsercookie.chrome()

#makeup the cookie string for the resqest
my_cookie=''
for cookie in cj:
    if '.meraki.com' in cookie.domain :
        if parrsed_url.netloc in cookie.domain :
            my_cookie = my_cookie + cookie.name + '=' + cookie.value + ';'
        elif 'two_factor_auth' in cookie.name :
            my_cookie = my_cookie + cookie.name + '=' + cookie.value + ';'
        elif 'dash_auth' in cookie.name :
            my_cookie = my_cookie + cookie.name + '=' + cookie.value + ';'
        elif '_gid' in cookie.name :
            my_cookie = my_cookie + cookie.name + '=' + cookie.value + ';'
        elif '_ga' in cookie.name :
            my_cookie = my_cookie + cookie.name + '=' + cookie.value + ';'


url = url_base+"manage/configure/guests"

headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.8,fr;q=0.6,ar;q=0.4",
            'connection': "keep-alive",
            'cookie': my_cookie ,
            'Upgrade-Insecure-Requests': '1'
        }

response = requests.request("GET", url, headers=headers)
#Save the html file in response
with open("Output.txt", "w") as text_file:
    text_file.write(response.text.encode('utf-8'))

#parse the response for the auth token
with open("Output.txt", "r") as text_file:
    for line in text_file:
        if 'Mkiconf.authenticity_token' in line :
            csrf_token = line.split('"')[1]

            #store cookie and token
            with open("meraki_env.json", "r+") as jsonFile:
                data = json.load(jsonFile)

                if data["csrf_token"] != csrf_token:
                    data["csrf_token"] = csrf_token
                    data["my_cookie"] = my_cookie
                    data["url_base"] = url_base
                    jsonFile.seek(0)  # rewind
                    json.dump(data, jsonFile)
                    jsonFile.truncate()
