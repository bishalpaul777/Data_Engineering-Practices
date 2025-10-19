# Video 23

# creating private methods

class Hello:
    def __init__(self,name):
        self.a = 10               # public variable
        self._b = 20              # protected variable (single underscore)
        self.__c = 30             # Private variable (double underscore)

    def public_method(self):
        print("This is a public method----")
        print("public value: ",self.a)
        print("private value: ",self.__c)
        self.__private_method()    # Calling the private in public method

    
    def __private_method(self):                    # created a private method
        print("This is a private method----")
        print("private value: ",self.__c)

hello = Hello('name')
print("public value: ",hello.a)
print("protected value:  ",hello._b)
# print(hello.__c)                          # we can't call a private member like this
hello.public_method()