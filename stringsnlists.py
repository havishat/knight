import math

'''def myfunction(str):
	x=str.split(" ");
	for i in range(0, len(x)):
		if x[i]== "day.":
			x[i]="month."
			break
	print x
	newstr = ""
	for word in x:
		newstr=newstr + word + " "
	print newstr

myfunction("It's thanksgiving day. It's my birthday,too!")


def minmax(numlist):
	print max(numlist)
	print min(numlist)

minmax([1,2,3,4])

def firstlast(anylist):
	print "first item: {}".format(anylist[0])
	print "last item: {}".format(anylist[-1])

firstlast([4,7,3,"cat"])'''


def listgymnastics(alist):
	alist.sort()
	divider= int(math.floor(len(alist)/2))
	listx=alist[0:divider]
	listy=alist[divider:len(alist)]
	listy+=[0]
	end=len(listy)-1
	print listy
	for i in range(end,-1,-1):
		listy[i]=listy[i-1]
	listy[0]=listx
	print listy


listgymnastics([1,2,3,4])
