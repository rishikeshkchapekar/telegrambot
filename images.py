import requests
import random

def getImages(query):
    query="toulouse pink city"
    r = requests.get("https://api.qwant.com/api/search/images",
        params={
            'count': 50,
            'q': query,
            't': 'images',
            'safesearch': 1,
            'locale': 'en_US',
            'uiv': 4
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    return urls