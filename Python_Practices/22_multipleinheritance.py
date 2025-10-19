# Video 25

# Multiple Inheritance  ---->

# import Teacher class from teacher file and Student class from student file --->

from teacher import Teacher
from student import Student

class Multi(Teacher,Student):
    def __init__(self,name,subject,roll):
        Teacher.__init__(self, subject)
        Student.__init__(self, roll)
        self.name = name
    
    def show_final(self):
        print("I am ",self.name)
        print("My subject is: ",self.get_subject())
        print("My Roll is: ",self.get_roll())


# objects -->

m = Multi('Bishal','Python',107)
m.show_teacher()
m.show_student()
m.show_final()