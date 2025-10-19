# Video 26 

# Python Super ---> 

class Parent:
    def __init__(self, name):
        print("Parent Class called....")    # 4. This will print
        print("This class made by ",name)   # 5. Then this print with argument value


class Child(Parent):
    def __init__(self):
        print("Child class called....")     # 2. This will print first
        super().__init__('Bishal')          # 3. This will call Parent class


child = Child()          # 1. Child Class object calling Child class
print(Child.__mro__)     


#__mro__ stands for Method Resolution Order.
# It is an attribute of a class that shows the order 
# in which Python looks for a method or attribute when it is called on an object.