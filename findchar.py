def findchar(letter,list):
	newlist=[]
	for word in list:
		if letter in word:
			newlist.append(word)
	print newlist

findchar('a',['hello','world','my','name','is','Anna'])
