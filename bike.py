class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed=max_speed
		self.miles = 0

	def displayinfo(self): 
		print "Price: {} Speed: {} Miles: {}".format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print "Riding"
		self.miles +=10
		return self
	
	def reverse(self):
		print "Reversing..."
		if self.miles>0:
			self.miles-=5
		else: 
			self.miles=0
		return self



bike1=Bike(100,20)
bike2=Bike(200,30)
bike3=Bike(50,20)

for i in range(3):
	bike1.ride()

bike1.reverse().displayinfo()

for i in range(2):
	bike2.ride().reverse()

bike2.displayinfo()

for i in range(3):
	bike3.reverse()
bike3.displayinfo()