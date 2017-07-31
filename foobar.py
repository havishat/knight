def foobar():
	bar=[]
	foobar=[]
	foo=[]
	for i in range(10,400):
		num=i**2
		if num<100000:
			bar+=[num]
		else:
			break
	
	for i in range(100,100000):
		if i not in bar:
			for x in range(2,i):
				if i%x==0:
					foobar+=[i]
					break
	for i in range(100,100000):
		if i not in bar and (i not in foobar):
			foo+=[i]

	for i in range(0,len(bar)):
		print "{} bar".format(bar[i])
	for i in range(0,len(foobar)):
		print "{} foobar".format(foobar[i])
	for i in range(0,len(foo)):
		print "{} foo".format(foo[i])

foobar()