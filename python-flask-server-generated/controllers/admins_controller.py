import requests
import json

def search_user(network = None):
	return_json = {"all_users":[]}
	url = network["url_base"]+"manage/configure/update_guests"

	querystring = {"send_emails":"true"}

	payload = {
	            'authenticity_token': network["csrf_token"],
	            'is_client_vpn': 'false',
	            'expiration_duration': '0',
	            'expires': 'false',
	            'expire_time': '',
	            'expire_units': '86400',
	            'ssid[number]': '1'
	            }
	headers = {
	    'accept': "*/*",
	    'accept-encoding': "gzip, deflate, br",
	    'accept-language': "en-US,en;q=0.8,fr;q=0.6,ar;q=0.4",
	    'connection': "keep-alive",
	    'content-type': "multipart/form-data;",
	    'cookie': network["my_cookie"],
	    'x-csrf-token': network["csrf_token"],
	    'x-requested-with': "XMLHttpRequest"
	    }

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	data = json.loads(response.text)
	for element in data["all_users"]:
		return_json["all_users"].append(data["all_users"][element])

	return return_json
