#Method overiding
class Vehicle:
    def showspeed(self):
        print("Faster than walking")
class Car(Vehicle):
    def showspeed(self):
        print("Faster than walking but on average 60 km/h")
class BulletTrain(Vehicle):
    def showspeed(self):
        print("Faster than walking but on average 200 km/h")

a = Vehicle()
a.showspeed()

# Now it's different, same showspeed method but different result
b = BulletTrain()
b.showspeed()