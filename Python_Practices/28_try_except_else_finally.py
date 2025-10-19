# Video 31

# Try  Except   Else   Finally  ---->

result = None

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    result = a/b
except ZeroDivisionError as z:
    print("ZeroDivisionError: ",type(z))
except TypeError as t:
    print("TypeError: ",type(t))
else:
    print("==Else Statement==")                  # execute when no error
finally:
    print("==Finally Statement==")               # execute anyway

print("result = ",result)
print("END")