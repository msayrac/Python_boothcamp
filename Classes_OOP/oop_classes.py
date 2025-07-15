"""
object oriented programing
"""

# class Student:
#     pass
#
# student_1 = Student()
# student_2 = Student()
#
# print(student_1)
# print(student_2)
#
# student_1.first_name = 'Eric'
# student_1.last_name = "Roby"
# student_1.major = "Computer Science"
#
# student_2.first_name = 'John'
# student_2.last_name = "Miller"
# student_2.major = "Math"
#
# print(student_1.first_name)
# print(student_2.first_name)
#
# print(student_1.last_name)
# print(student_2.last_name)
#
# print(student_1.major)
# print(student_2.major)


class Student:
    # class variable
    school = "Online School"

    number_of_students = 0

    def __init__(self,first_name,last_name,major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        Student.number_of_students += 1

    def fullname_with_major(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major!"

    def fullname_major_school(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major going to {self.school}!"

    @classmethod
    def set_online_school(cls,new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls,student_str):
        first_name, last_name, major = student_str.split(".")
        return cls(first_name,last_name,major)


student_1 = Student("Mike", "Smith","Computer Science")
student_2 = Student("James", "Miller","Math")


print(student_1.first_name)
print(student_2.first_name)

print(student_1.fullname_with_major())
print(student_2.fullname_with_major())

print(Student.fullname_with_major(student_1))


"""class variables """

print(student_1.school)
print(student_2.school)

print(student_1.fullname_major_school())

print(Student.fullname_major_school(student_2))

print(f"Number of students = {Student.number_of_students}")

print(student_1.school)
print(student_2.school)

Student.set_online_school("I use Google Hangouts for class!")
print(student_1.school)
print(student_2.school)

new_student = "Adam.yuztz.English"

student_3 = Student.split_students(new_student)
print(student_3.first_name,student_3.last_name,student_3.major)

print(Student.number_of_students)
print(student_3.fullname_major_school())












