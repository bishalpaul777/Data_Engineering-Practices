# Video 10

# Sets in python ---->


# not include duplicate values
A = {1 , 8 , 4 , 3 , 1, 5}          
print(A)                         


# length of the set.
print(len(A))                  


# Adding a single value
A.add(12)                       
print(A)                   


# Adding multiple values
A.update([21, 19, 15])          
print(A)


# removing a value
A.remove(12)                    
print(A)


# remove random value
A.pop()            
print(A)


name = {'max','bob','Astin'}
print(name)
# clear all the value
name.clear()             
print(name)


# converting list into set
lst = set([41,45,48,49])     
print(type(lst))


# Union, Intersection op --->
x = {42,45,57,60}
y = {95,42,57}

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
    
