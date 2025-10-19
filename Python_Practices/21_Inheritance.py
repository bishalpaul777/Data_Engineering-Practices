# Video 24

# Python Inheritance ---->

class polygon:                                        # Polygon class
    __width = None                                    # private members
    __height = None


    def set_values(self,height,width):                # setter method
        self.__height = height
        self.__width = width

    def get_width(self):                              # getter method
        return self.__width
    def get_height(self):
        return self.__height
    


class rectangle(polygon):                             #  Rectangle inherit
    def area(self):
        return self.get_height() * self.get_width()


class triangle(polygon):                             # triangle inherit
    def area(self):
        return (self.get_height() * self.get_width())/2


rect = rectangle()
tri = triangle()

x = int(input("Enter height: "))
y = int(input("Enter width: "))

rect.set_values(x,y)
tri.set_values(x,y)

print("Area of triangle is: ",tri.area())
print("Area of rectangle is: ",rect.area())