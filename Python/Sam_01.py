# Write a python class Student with following data members:
# ● name - student name
# ● roll_no - student roll no
# ● marks - student marks in list data type for 3 subjects
# The class should support the following methods:
# (i) __init__() - to initialize data members
# (ii) display() - to display the details of the student
# (iii) marksAvg() - return the average marks of the student

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
    
    def marksAvg(self):
        return sum(self.marks) / len(self.marks)
s1 = Student("Anubhav", 16122, [95, 95, 98])
s1.display()
print(f"Average marks: {s1.marksAvg()}")
