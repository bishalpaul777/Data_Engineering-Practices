# Video 38

# Python Decorators

def my_decorator(func):
    def my_wrapper():
        print("Befor the function runs...")
        func()
        print("After the function runs...")
    return my_wrapper

@my_decorator
def hello():
    print("Hello sir...")

hello()


def decorator_div(func):
    def wrapper_div(a, b):
        print("Divide",a,"by",b)

        if(b==0):
            print("Division done by 0 is not allowed")
            return
        return a/b
    return wrapper_div

@decorator_div
def div(x,y):
    return x/y

print(div(15,0))

