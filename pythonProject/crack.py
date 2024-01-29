# def palindrome(str1, str2):
#     return str1 == str2[::-1]

# str1 = input("Enter the string1: ")
# str2 = input("Enter the string2: ")

# if palindrome(str1, str2):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

class Human:
    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def display_human(self):
        print(f"The Name of student is : {self.name},The Age of student is: {self.age} The roll_no of student is {self.rollno}")

class  Student(Human):
    def  __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

    def  get_rollno(self):
        print (f"Roll No of student is : {self.rollno}")

student1 = Student("John", 25, "007")
student1.display_human ()