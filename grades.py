import random

def grades():
	gradelist=[]
	print gradelist
	for i in range(10):
		x= random.randint(60,100)
		gradelist+=[x]
	scores={}
	for z in range(0, len(gradelist)):
		if gradelist[z]>=90:
			scores[gradelist[z]]="A"
		elif gradelist[z]>=80:
			scores[gradelist[z]]="B"
		elif gradelist[z]>=70:
			scores[gradelist[z]]="C"
		elif gradelist[z]>=60:
			scores[gradelist[z]]="D"
	print scores

grades()