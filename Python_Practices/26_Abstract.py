# Video 29

# Abstract classes ----->

from abc import ABC,abstractmethod          # importing ABC module & abstract method
class Shape(ABC):                           # inherit the properties of ABC module
    @abstractmethod                         # initialize the abstract method to every methods
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape):

    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4*self.side

square = Square(5)

print("Area of the square is: ",square.area())
print("Perimeter of the square is: ",square.perimeter())