

def mult(): #define function
	for i in range(1,1001): #loops over the numbers from 1 to 1000
		if i%2 is not 0: #checks if number is odd
			print i

mult() #function call

def mult2(): #define function
	for i in range(5,1000001): #loops over the numbers from 5 to 1 million
		if i%5 is 0: #checks if number is divisible by 5
			print i

mult2() #function call 

def sigma(mylist):
	sum=0
	for i in range(0,len(mylist)): #loops over my list
		sum+=mylist[i] #adds list value to a sum
	print sum #prints the total

sigma([1, 2, 5, 10, 255, 3])


def mean(mylist):
	sum=0
	for i in range(0,len(mylist)): #this loop sums the values
		sum+=mylist[i]
	print sum/(len(mylist)) #divide the sum of the values by the length of the array

mean([1, 2, 5, 10, 255, 3])



