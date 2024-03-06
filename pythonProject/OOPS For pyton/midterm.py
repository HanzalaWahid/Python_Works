pi = 3.142
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Calculate_area(self):
        self.area = pi * self.radius **2

    def Calculate_perimeter(self):
        self.perimeter = 2 * pi * self.radius**2

    def display(self):
        print(f"The area is {self.area} and the perimeter is {self.perimeter}")



c1 = Circle(4)
c1.Calculate_area()
c1.Calculate_perimeter()
c1.display()

class Furniture:
    def properties(self):
        pass

class Table(Furniture):
    print("")
