class Animal(object):
    """
    Animal class that displays health, used as parent class for other classes
    
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self
    
    def displayHealth(self): 
        print "health", self.health
        return self


class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name, 150)
    
    
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name, 170)
    
    def fly(self):
        self.health-=10
        return self
    
    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print "I am a Dragon"

print "ZEBRA"
animal=Animal("Zebra", 100)
animal.displayHealth()
animal.walk().walk().walk().run().run().displayHealth()        

print "DOG"
dog = Dog("Corgi")
dog.displayHealth()
dog.walk().walk().walk().run().run().pet().displayHealth()

print "DRAGON"
dragon = Dragon("Eragon")
dragon.displayHealth()
dragon.fly().run().run().displayHealth()