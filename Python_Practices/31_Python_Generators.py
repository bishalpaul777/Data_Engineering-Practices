# Video 34

# Python Generators ---->

def fun():
    for i in range(5):
        yield i

x = fun()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


def list_iter(list):
    for i in list:
        yield i


a = [1,7,9,6,2]

list = list_iter(a)

print(next(list))
print(next(list))
print(next(list))