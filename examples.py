class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "Price:", self.price
        print "Max speed:", self.max_speed
        print "Total miles:", self.miles
    
    def ride(self):
        print "Riding"
        self.miles+=10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles-5 <= 0:
            self.miles=0
        else:
            self.miles-=5
        return self

print "BIKE 1"
bike1 = Bike(200, "25mph")
bike1.displayInfo()
bike1.ride().ride().ride().reverse()
bike1.displayInfo()

print "BIKE 2"
bike2 = Bike(250, "30mph")
bike2.ride().ride().reverse().reverse()
bike2.displayInfo()

print "BIKE 3"
bike3 = Bike(100, "28mph")
bike3.reverse().reverse().reverse()
bike3.displayInfo()