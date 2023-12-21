class Student:
    def __init__(self, Id, Name, Dept, Roll_No):
        self.Id = Id
        self.Name = Name
        self.Dept = Dept
        self.Roll_NO = Roll_No

    def __str__(self):
        return f"the Id of person is {self.Id}, the name is {self.Name}, the department of person is {self.Dept}, and the roll_no is {self.Roll_NO}"


class Exam_Dept(Student):
    def __init__(self, Id, Name, Dept, Roll_No, Section, Total_Subjects):
        super().__init__(Id, Name, Dept, Roll_No)
        self.Section = Section
        self.Total_Subjects = Total_Subjects

    def __str__(self):
        return f"{super().__str__()} {self.Section} and total subject study is {self.Total_Subjects}"


s1 = Exam_Dept(1, "John", "Math", 101, "A", 5)
s2 = Exam_Dept(2, "Alice", "Physics", 102, "B", 4)
s3 = Exam_Dept(3, "Bob", "Chemistry", 103, "C", 6)

print(s1)
print(s2)
print(s3)
