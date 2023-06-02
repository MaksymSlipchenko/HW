class PlaceHolder:
    pass

class Student:

    course = 2

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'Name: {self.name}'

    @staticmethod
    def get_course():
        print(f'Course: {Student.course}')


class StudentGrades(Student):
    def __init__(self, name, math):
        Student.__init__(self, name)
        self.math = math

    def get_math_grade(self):
        return f'Math grade: {self.math}'

vova = StudentGrades('Vova', '5')
print(vova.get_name())
Student.get_course()
print(vova.get_math_grade())

