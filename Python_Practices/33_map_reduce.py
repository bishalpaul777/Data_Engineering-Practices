# Video 36

# lambda --->

# double a value using lambda --->
double = lambda x : x*2
print(double(10))

# checking even odd
check = lambda x: "Even" if x%2==0 else "odd"
print(check(52))


# map function
lst1 = [1,6,7,9,4]
lst2 = [5,8,3,4,2]

# adding 10 to all the values of the list
a = map(lambda x: x+10,lst1)    
print(list(a))

# multiplying the two list
b = map(lambda x,y: x*y,lst1,lst2)
print(list(b))



# Filter Function ---->
c = filter(lambda x:x%2==0,lst1)
print(list(c))

d = filter(lambda x: x>4,lst1)
print(list(d))



# Reduce Function ---->
from functools import reduce
r = reduce(lambda x,y:x+y,lst1)
print(r)

r1 = reduce(lambda x,y:x*y,lst1)
print(r1)