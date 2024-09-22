class Car:
    def __init__ (self, make, max_speed):        
        self.speed = 0
        self.make = make
        self.max_speed = max_speed

    def display_speed(self):
        print(self.speed)
    
    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 10

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
        return self.speed
    
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()