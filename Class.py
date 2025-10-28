class Class:
    student = []
    total_cgpa = 0

    def __init__(self, name):
        self.name = name

    def add_student(self, this_student):
        self.student.append(this_student)

    def get_students_info(self):
        print(self.name)
        for i in range(0, len(self.student)):
            print(f"student {i + 1}")
            print(self.student[i].get_info())

    @classmethod
    def get_count(cls):
        return len(cls.student)

    @classmethod
    def average_cgpa(cls):

        if cls.get_count() == 0:
            return 0

        total = 0
        for i in range(0, len(cls.student)):
            total += cls.student[i].gpa

        average_cgpa = total / cls.get_count()

        return f"The average cgpa {average_cgpa}"


class Student:
    def __init__(self, name, gpa, Class_lecture):
        self.name = name
        self.gpa = gpa
        Class_lecture.add_student(self)

    # INSTANCE METHOD
    def get_info(self):
        return f"Name {self.name} gpa {self.gpa} \n"


class_one = Class("Object Oriented Programming")

student_one = Student("Muna", 3.9, class_one)
student_two = Student("Issa", 3.5, class_one)
student_three = Student("Ahmed", 4.0, class_one)
student_four = Student("Mikey", 3.6, class_one)

class_one.get_students_info()
print(class_one.average_cgpa())
