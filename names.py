'''def name1(x):
	for i in x:
		for z in i:
			print "My {} is:{}".format(z, i[z])

name1( [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
])'''

def name2(y):
	count=1
	print "Students"
	for i in y["Students"]:
		mystr=""
		mystr=mystr + i["first_name"] + " "
		mystr+=i["last_name"]
		print "{}-{} - {}".format(count, mystr,len(mystr))
		count+=1
	count=1
	print "Instructors"
	for i in y["Instructors"]:
		mystr=""
		mystr=mystr + i["first_name"] + " "
		mystr+=i["last_name"]
		print "{}-{} - {}".format(count, mystr,len(mystr))
		count+=1

	
			




name2( {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
)