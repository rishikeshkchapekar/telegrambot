import requests
from datetime import datetime
import json
from urllib.parse import urlparse
import os
import uuid
from os.path import splitext, basename
import random
client_id = os.environ['imgur_id']

queried ={}
h=open('queried.txt','r')
hData=h.read()
try:
    queried = json.loads(hData)
except:
    print("No existing queried data")    
h.close()
def download(url):
    disassembled = urlparse(url)
    filename, ext = splitext(basename(disassembled.path))
    name=str(uuid.uuid4())
    with open(name+ext, 'wb') as f:
        with requests.get(url, stream=True) as r:
            for chunk in r.iter_content():
                f.write(r.content)
    return name+ext
def upDateQueries(searchterm,qType):
    now = datetime.now() 
    f=open("pexels_queries.txt","a")    
    f.write(f"{now},{searchterm},{qType}\n")
    f.close()
def setNewItem(jsonString):
    g=open('queried.txt','w')
    g.write(jsonString)
    g.close()    
def getPhoto(query):
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
    url=img['link']
    return url
