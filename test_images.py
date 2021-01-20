import requests
import os
import json
import random

client_id = os.environ['imgur_id']

def getImage(query):
	url="https://api.imgur.com/3/gallery/search/top/0"
	params={
		"q": query
	}
	headers={
		'Authorization':f'Client-ID {client_id}'
	}
	response = requests.get(url,headers=headers,params=params)
	resp = response.text
	jsonData = json.loads(resp)
	data = jsonData['data']
	img = random.choice(data)
	print(list(img.keys()))
	url=img['link']
	return url