# Video 16


# Builtin and userdefined function in python ----



# Builtin function ----
print("Hello, Bishal!")       # prints output
numbers = [10, 20, 30]
print(len(numbers))           # length → 3
print(sum(numbers))           # sum → 60
print(max(numbers))           # maximum → 30



# Userdefined Function

#summation
def sum(i,j):
    return i+j

x = 16
y = 42
print("Sum is:  ",sum(x,y))


# Greetings ---
def greet(x):
    print("Hello! ",x)

name = input("Enter your name: ")
greet(name)