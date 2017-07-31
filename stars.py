def stars(x):
	for i in x:
		mystr=""
		if type(i) is int:
			print "*"*i
		elif type(i) is str:
			for z in range(len(i)):
				mystr+=(i[0])
			print mystr

stars([4,5,6, "cat"])