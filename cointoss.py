import random
def coin():
	heads=0
	tails=0
	for i in range(0,5000):
		print "attemt #{}".format(i)
		x=random.randint(0,1)
		if x==0:
			heads+=1
			print"Throwing a coin... It's a head! You have {} heads and {}tails!".format(heads,tails)
		elif x==1:
			tails+=1
			print"Throwing a coin... It's a tail! You have {} heads and {}tails!".format(heads,tails)
	print "Ending the program, thank you!"

coin()