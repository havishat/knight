def comparearrays(arr1, arr2):
	if len(arr1) <> len(arr2):
		print "The lists are not the same"
		return
	for i in range (0, len(arr1)):
		if arr1[i]<>arr2[i]:
			print "The lists are not the same"
			return
	print "The lists are the same"

comparearrays([1,2,3,4],[1,2,3,"x"])

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
comparearrays(list_one,list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
comparearrays(list_one,list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
comparearrays(list_one,list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
comparearrays(list_one,list_two)
