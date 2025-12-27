class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks 

    def talk(self):
        print("My name is:",self.name)
        print("My roll number is:",self.roll_no)
        print("My marks are:",self.marks)

s = Student("RK Sahu",44,90)
print(s.name,s.roll_no,s.marks)


class Test:
    def __init__(self):
        print("address of object by self:",id(self))

t=Test()
print("address of object by t:",id(t))
