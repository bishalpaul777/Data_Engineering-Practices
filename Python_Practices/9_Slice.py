# Video 12

# Slice

a = [0,1,2,3,4,5,6,7,8]
b = (0,1,2,3,4,5,6,7,8)
c = 'newzealand'

# showing values from index 0 to 5
print(a[0:6]) 


# showing value from index 2 to the rest
print(b[2:])


# showing the values by skipping one-middle value
print(a[0::2])


# slicing the string
print(c[0:6])


# negative index value, negative index starts from right hand side
print(a[-3])
print(c[-5])


# reverse order using negative indexing
print(c[::-1])