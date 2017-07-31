def typelist(mylist):
	sums = 0;
	strings = ""
	didnum=False
	didstr=False
	for i in range(0,len(mylist)):
		a=type(mylist[i])
		if a is int:
			sums+=mylist[i]
			didnum=True
		if a is str:
			strings+=mylist[i]
			didstr=True
	if didnum and didstr:
		print "The list you entered was of mixed type"
		print "Strings={}".format(strings)
		print "Sum={}".format(sums)
	elif didnum:
		print "The list you entered was of integer type"
		print "Sum={}".format(sums)
	elif didstr:
		print "the list you entered was of string type"
		print "Strings={}".format(strings)

typelist([4,17,"dog"])