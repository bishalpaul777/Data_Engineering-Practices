# Video 37

# Nested Function

def outer():                                  # Outer Function
    message = " Hello I am from outer"

    def inner():                              # Inner Function
        print("The inner says: ",message)
    
    inner()                                   # Calling the inner fn

outer()                                       # Calling the outer fn





def npow(exponent):                  # outer fn
    def pow_base(base):              # inner fn
        return pow(base, exponent)
    return pow_base                  

square = npow(2)             # call the outer fn
print(square(3))
