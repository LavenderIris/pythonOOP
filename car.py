class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price>10000:
            self._tax = 0.15
        else:
            self._tax = 0.12
        #self.displayAll()

    def __repr__(self):
        return '<User object price:{}, speed: {}, fuel: {}, mileage: {} tax: {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", str(self.speed)+"mph"
        print "Fuel:", self.fuel
        print "Mileage:",str(self.mileage)+"mpg"
        print "Tax:", self._tax



if __name__ == "__main__":
    # creation and display of all my instances of Car
    car1 = Car(2000, 35, 'Full', 15)
    car2 = Car(2000, 5, 'Not Full', 105)
    car3 = Car(2000, 15, 'Kind of Full', 95)
    car4 = Car(2000, 25, 'Full', 25)
    car5 = Car(2000, 45, 'Empty', 25)
    car6 = Car(20000000, 35, 'Empty', 15)