import store
import product
import mathDojo
import car
import animal
import hospital

if __name__ == "__main__":
    item1 = product.Product(10,"cat toy",5,"Fisher", 5)
    print item1
    target = store.Store([],"sunnyvale", "mr T")
    print target
  
    md=mathDojo.MathDojo()
    md.add(2).add(2,5).subtract(3,2)
    print md

    car1 = car.Car(2000, 35, 'Full', 15)
    print car

    animal1=animal.Animal("Zebra", 100)
    dragon = animal.Dragon("Eragon")
    dog = animal.Dog("Corgi")
    print animal1
    print dragon
    print dog

    patient1 = hospital.Patient(1, "Dinosaur Rex","peanuts")

    hospital=hospital.Hospital("General", 10)
    print patient1
    print hospital