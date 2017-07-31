'''def odd_even():
	oddeven={}
	for i in range(1,2001):
		if i%2 ==0:
			oddeven[i]="even"
		else:
			oddeven[i]="odd"
	print oddeven

odd_even()'''

def multiply(a,b):
	newarr=[]
	for i in range(0, len(a)):
		newarr+=[a[i]*b]
	print newarr


multiply([2,3,4,5],2)


