from youtube_search import YoutubeSearch
import json

def getVideo(search):
	results = YoutubeSearch(search, max_results=10).to_json()
	results =json.loads(results)
	result = results['videos'][0]
	suffix = result['url_suffix']
	url = f"https://www.youtube.com{suffix}"
	return url