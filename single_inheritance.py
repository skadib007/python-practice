class Car:
    colour ="black"
    @staticmethod
    def start():
        print("car is starting")
    def stop(self):
        print("car is stopping")

car1 = Car()
print(car1.colour)
car1.start()
car1.stop() 