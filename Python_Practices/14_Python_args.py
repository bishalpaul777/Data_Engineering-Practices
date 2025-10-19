# Video 17

# Python Arguments ---->

# Python default arguments --->
def student(name='unknown name',age='0'):
    print("name: ",name)
    print("Age: ",age)

student()


print("\n")

# multiple values in a single argument. 
# Single * args--->
def result(name,age, *marks):
    print("name: ",name)
    print("age: ",age)
    print("marks: ",marks)

result('Tom',16,85,92,45,75)

print("\n")


# double ** args-->
def office(name,id,**skills):
    print("name: ",name)
    print("id: ",id)
    # print("skills: ",skills)
    for key,value in skills.items():
        print(key,'= ',value)

office('Max',1021,python=8,C=7,java=9)


