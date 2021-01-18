import wikipedia

def getInfo(searchterm):
	print("SEARCH",searchterm)
	res = wikipedia.search(searchterm)
	print(res)
	relevant=res[0]
	page=wikipedia.page(relevant)
	summary = page.summary
	title = page.title
	return f"Here's some info on {title}:\n\n\n{summary}"