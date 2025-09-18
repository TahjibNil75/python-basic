# Class Method = Allow operations related to class itself
#                Take (cls) as first parameter, which represents the class itself


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def details(self):
        return f"Student Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
        
    @classmethod
    def student_count(cls):
        return f"Total Students: {cls.count}"
    

student1 = Student("Alice", 3.5)
student2 = Student("Bob", 3.8)
student3 = Student("Charlie", 3.2)
print(student1.details())
print(Student.student_count())
print(Student.average_gpa())