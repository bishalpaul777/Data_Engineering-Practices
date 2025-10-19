# Video 21


# multiple constructor ---->

def student_info(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# calling the function
student_info("Bishal", 25, "Kolkata","West Bengal", course="Python",roll_no = "OP124", grade="A+", active=True)
