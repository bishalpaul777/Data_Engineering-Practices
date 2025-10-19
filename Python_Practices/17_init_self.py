# Video 20

# init self in class

# Class Car ---->

class car:
    def __init__(self,name,color,speed):         # variables inside class
        self.name = name
        self.color = color
        self.speed = speed

    
    def display(self):                  # method inside class
        print(f"Car name: {self.name}     Color is: {self.color}       Speed is: {self.speed}")


ford = car("Ford","black",280)
audi = car("Audi","Red",320)
ferrari = car("Ferrari","blue",380)

ford.display()
audi.display()
ferrari.display()