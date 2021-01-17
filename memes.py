import praw 
import random
import os
clientId=os.environ['client_id']
clientSecret=os.environ['client_secret']
userAgent=os.environ['user_agent']
reddit = praw.Reddit(client_id=clientId,client_secret=clientSecret,user_agent=userAgent)

subreddits={
	"regular":["memes","greentext","Animemes"],
	"dank":["dankmemes","cursedcomments","4chan"],
	"relatable":["meirl"],
	# "facepalm":"facepalm"
}

def getMemeUrl(category):
	categories = list(subreddits.keys())
	if category not in categories:
		category="regular"
	print(category)	
	subred = reddit.subreddit(random.choice(subreddits[category]))
	posts = subred.top(limit=10)
	posts=list(posts)
	r=random.randint(0,len(posts))
	post=posts[r]
	url = post.url
	return url