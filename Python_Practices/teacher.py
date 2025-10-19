# teacher file

class Teacher:
    def __init__(self,subject):
        self.__subject = subject

    def show_teacher(self):
        print("I am a teacher.")

    def get_subject(self):
        return self.__subject
    