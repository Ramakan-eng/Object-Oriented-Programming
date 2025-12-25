class Student:
    def __init__(self):
        self.name = "RK Sahu"
        self.roll_no = 44
        self.marks = 90

    def talk(self):
        print("My name is:",self.name)
        print("My roll number is:",self.roll_no)
        print("My marks are:",self.marks)

s = Student()
print(s.name)
print(s.roll_no)
print(s.marks)
s.talk()
