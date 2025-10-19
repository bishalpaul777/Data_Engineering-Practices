# Video 30

# Exception Handling ---->

result = None

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    result = a/b
except ZeroDivisionError as z:
    print("ZeroDivisionError: ",type(z))
except TypeError as t:
    print("TypeError: ",type(t))

print("result = ",result)
print("END")