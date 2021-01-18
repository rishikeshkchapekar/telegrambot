import os
import praw 
import random

config = {
	"client_id": os.environ["client_id"],
	"client_secret": os.environ["client_secret"],
	"user_agent": os.environ["user_agent"],
}

reddit = praw.Reddit(**config);

def getMemeUrl(category):
	subred = reddit.subreddits.search_by_name(category)[0]
	posts = list(subred.top(limit=10))

	post = random.choice(posts)
	return post.url
