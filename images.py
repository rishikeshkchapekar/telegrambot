import requests
from datetime import datetime
import json
from urllib.parse import urlparse
import os
import uuid
from os.path import splitext, basename
api_key=os.environ['api_key']

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
def getPhoto(searchterm):
    terms = queried.keys()
    if searchterm in terms:
        upDateQueries(searchterm,"repeat")
        return queried[searchterm]
    else:    
        pics = list()
        url="https://api.pexels.com/v1/search"
        data={
            'query': searchterm,
            'per_page': 200
        }
        headers={
            'Authorization': api_key
        }
        response = requests.get(url,headers=headers,params=data)
        resp = response.text
        resp = json.loads(resp)

        for photos in resp['photos']:
            photographer = photos['photographer']
            photographer_url = photos['photographer_url']
            img_url = photos['src']['medium']
            pic = (img_url,photographer,photographer_url)
            pics.append(pic)
        queried[searchterm]=pics
        qJson = json.dumps(queried)
        upDateQueries(searchterm,"new")
        setNewItem(qJson)   
        return pics
