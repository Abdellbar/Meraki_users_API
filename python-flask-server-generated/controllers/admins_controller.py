import requests
import json

def search_user(network = None):
	return_json = {"all_users":[]}
	url = network["url_base"]+"manage/configure/update_guests"

	querystring = {"send_emails":"true"}

	#payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"authenticity_token\"\r\n\r\n"+csrf_token+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"is_client_vpn\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"expiration_duration\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"expires\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"expire_time\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"expire_units\"\r\n\r\n86400\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ssid[number]\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
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
	    'content-type': "multipart/form-data;", #boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
	    'cookie': network["my_cookie"],
	    'x-csrf-token': network["csrf_token"],
	    'x-requested-with': "XMLHttpRequest"
	    }

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	data = json.loads(response.text)
	for element in data["all_users"]:
		return_json["all_users"].append(data["all_users"][element])

	return return_json
