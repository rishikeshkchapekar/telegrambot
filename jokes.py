import pandas as pd
import random

data = pd.read_csv('jokes.csv')
ques = data['Question'].tolist()
ans = data['Answer'].tolist()

def getJoke():
	r = random.randint(0,len(ques))
	q = ques[r]
	a = ans[r]
	joke = f"Q:{q}\nA:{a}"
	return joke