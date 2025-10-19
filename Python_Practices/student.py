# student class

class Student:
    def __init__(self,roll):
        self.__roll = roll

    
    def show_student(self):
        print("i am a student.")

    def get_roll(self):
        return self.__roll
