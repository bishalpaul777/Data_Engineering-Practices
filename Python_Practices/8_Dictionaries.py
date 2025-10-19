# Video 11

# Python Dictionaries ---->

# Creating dictionary
D = {'name':'Max','Roll':12,'age':15}
print(D)


# showing the value referring the key
print(D['name'])


# get method
print(D.get("age"))


# Update a value
D["name"] = "Ram"
print(D)


# Add a new pair
D["surname"] = "sampath"
print(D)


# Delete a pair
D.pop("Roll")
print(D)


# Lists the keys only
print(D.keys())


# Lists the Values only
print(D.values())


# To remove the last updated value or pair
print(D.popitem())
print(D)


# Clear the Dictionary
D.clear()
print(D)


# Delete the dictionary
del D
print(D)   # Will give an error