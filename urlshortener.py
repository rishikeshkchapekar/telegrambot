import requests
import json
import os

api_key=os.environ['bitly_api']

def shortenUrl(long_url):
	url="https://api-ssl.bitly.com/v4/shorten"
	headers={
		'Authorization':f'Bearer {api_key}',
		'Content-Type':'application/json'
	}
	data={
		'long_url':long_url
	}
	resp=requests.post(url,headers=headers,json=data)
	resp_data=resp.text
	resp_data=json.loads(resp_data)
	return resp_data['link']