def mult():
	w, h = 12, 12;
	table = [[0 for x in range(w)] for y in range(h)] 
	for x in range(1,13):
		for y in range(1,13):
			table[x-1][y-1]=x*y
	print table

mult()
