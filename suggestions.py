
def registerSuggestion(msg):
	if(msg.strip() == "/suggestion"):
		retMsg = "Nope...unacceptable. That's a blank suggestion\n\n"
		retMsg += "Here's a tip: \n\nInstead of just tapping on that command...why don't you actually type the word '/suggestion' and actually TYPE SOME SHIT IN FRONT OF IT?"
		return retMsg
	else:
		f=open('suggestions.txt','a')
		f.write(msg+'\n')
		f.close()
		return "Noted"