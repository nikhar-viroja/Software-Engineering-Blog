class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_subject(self):
        return self.subject


# Create a student and a teacher object
student = Student("John", 16, "A")
teacher = Teacher("Ms. Smith", 35, "Math")

# Print information about the student and teacher
print("Student name:", student.get_name())
print("Student age:", student.get_age())
print("Student grade:", student.get_grade())
print("Teacher name:", teacher.get_name())
print("Teacher age:", teacher.get_age())
print("Teacher subject:", teacher.get_subject())
