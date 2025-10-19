# Video 7

# Nested If

x = int(input("Enter a number....."))

if x > 10:
    print("x is greater than 10")
    if x < 20:
        print("x is also less than 20")
    else:
        print("x is 20 or more")
else:
    print("x is 10 or less")


x = int(input("Enter a number:   "))

if x<0:
    print("Number is negative...")
elif(x%2==0):
    print("x is even...")
else:
    print("X is odd...")