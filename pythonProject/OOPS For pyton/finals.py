class Shape:
    pie = 3.142

    def properties(self,color,position):
        self.color = color
        self.position = position

class Circle(Shape):
    def __init__(self,radius,color,position):
        self.radius = radius
        self.properties(color,position)

    def area_of_circle(self):
        self.area = self.pie * self.radius ** 2

    def display(self):
        print(f"The area of circle is: {self.area} the color is {self.color} and the position is {self.position}")
class Rectangle(Shape):
    def __init__(self,length,width,color,position):
        super().__init__()
        self.length = length
        self.width = width
        self.properties(color,position)

    def area_of_rectangle(self):
        self.area = self.length * self.width

    def display(self):
        print(f"The area of recatangle is {self.area} the color is {self.color} and the color is {self.position}")

c1 = Circle(4,"blue","middle")
c1.area_of_circle()
c1.display()


c2  = Rectangle(6,7,"yellow","center")
c2.area_of_rectangle()
c2.display()


class Zoo:
    def Properties (self,name,age,healthstatus):
        self.name = name
        self.age = age
        self.healthstatus = healthstatus

class Mammals(Zoo):
    def Have_Hair(self,name,age,healthstatus):
        self.Properties(name,age,healthstatus)

    def dispaly(self):
        print(f"The name of mammal is {self.name} the age is {self.age}  and the helath status {self.healthstatus}")

class Bird (Zoo):
    def Have_Fur(self,name,age,healthstatus):
        self.Properties(name,age,healthstatus)

    def dispaly(self):
        print(f"The name of mammal is {self.name} the age is {self.age}  and the helath status {self.healthstatus}")

class Reptile (Zoo):
    def Have_Scale(self,name,age,healthstatus):
        self.Properties(name,age,healthstatus)

    def dispaly(self):
        print(f"he name of mammal is {self.name} the age is {self.age}  and the helath status  {self.healthstatus}")

z1 = Mammals()
z1.Have_Hair("Goat",12,'alive')
z1.dispaly()

z2 = Reptile()
z2.Have_Scale("snake",3,'dead')
z2.dispaly()

z3 = Bird()
z3.Have_Fur("Eagle",8,'alive')
z3.dispaly()

class Person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self._id = id

    def display(self):
        print(f"The name is {self.name} age is {self.age} and the id of person is {self._id}")

class Student(Person):
    def __init__(self,name,age,id,marks):
        super().__init__(name,age,id)
        self.marks = marks

    def display(self):
        super(Student, self).display()
        print("The marks obtain is",self.marks)

p1 = Person("Hanzala",19,"20CEt-106")
s1 = Student("Mashoood",20,"AIC0-123",98)
s1.display()
p1.display()

