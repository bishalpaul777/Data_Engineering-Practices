# Video 8

# Lists operations ---->

lst = [4,5,7,"India",78,"Jai Hind"]

print(lst)         #List view

print(lst[4])       # show the 4th index of the list

print(lst[1:6:2])   # slicing, it will starts from index 1 till 5. 
                    # Show the 2nd value of the first.

print(len(lst))     # Show the length


lst.append("Jai Bharat")   # Add a new value
print(lst)

lst.insert(3,"Dev")        # by insert() we can insert the value in specific location
print(lst)

lst.remove("Dev")          # by this remove(), we can remove the value we want
print(lst)

lst.pop()                  # pop() will remove the last element.
print(lst)




lst2 = [2,7,9,4]         
print(lst2)

lst2.sort()                # sort the list
print(lst2)
 
lst2.reverse()             # Reverse the list
print(lst2)

lst2.clear()              # clear the value of the list
print(lst2)