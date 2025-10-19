# Video 22

# Python encapsulation

class rectangle:
    def __init__(self,height,width):
        self.__height = height                # private variable (__)
        self.__width = width
    
    def set_height(self,height):              # use set method to set value for private
        self.__height = height
    
    def get_height(self):                     # use get method to get value for private
        return self.__height

    def set_width(self,width):
        self.__width = width
    
    def get_width(self):
        return self.__width
    
    def get_area(self):
        return self.__height*self.__width

h = int(input("Enter the height:  "))
w = int(input("Enter the width:  "))
rect = rectangle(h,w)

print("The height of the rectangle is: ",rect.get_height())
print("The width of the rectangle is: ",rect.get_width())
print("The area of the rectangle is:  ",rect.get_area())
    
