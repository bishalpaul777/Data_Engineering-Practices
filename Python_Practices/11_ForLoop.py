# Video 14

# Python For Loop   ---->

lst = [0,1,2,3,4,5,6]
tup = (0,1,2,3,4,5,6)
dic = { 'name': 'Prabhu',
       'address': 'Mumbai'
}

# printing the value of list
print("list values are:  ",end=" ")
for i in lst:
    print(i,end=" ")


print("\n")


# each value of tuple multiply by 5
print("tuples value multiply by 5:  ",end=" ")
for i in tup:
    print(i*5,end=" ") 

print("\n")


# printing only even number from the list
print("The even number of the list are:  ",end=" ")
for i in lst:
    if(i%2==0):
        print(i,end=" ")


print("\n")


# printing the keys of a dictionary 
print("Keys are:  ")
for x in dic.keys():
    print(x,end=" ")


print("\n")


# printing the values ---
print("The values are:  ")
for x in dic.values():
    print(x,end=" ")


print("\n")


# printing key value together ---
for key,value in dic.items():
    print(key,': ',value)


print("\n")


# printing in between range ---
for i in range(10):
    print(i,end="  ")

print("\n")

# printing from 1 to 40 with a gap of 6 ---
for i in range(1,40,6):
    print(i,end="  ")