class Laptop:
    def properties(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price 

    def show(self):
        print("Brand Name: ", self.brand_name)
        print("Model Name: ", self.model_name)
        print("Price: $", self.price)


# Creating object of the class laptop
my_laptop = Laptop()
my_laptop.properties("Hp", "570", 10000)
my_laptop.show()


class Mobile(Laptop):
    def os(self, os_type):
        self.os_type = os_type


# Creating Object of the sub-class mobile
my_mobile = Mobile()
my_mobile.properties("Samsung", "Galaxy S21", 9000)
my_mobile.show()
my_mobile.os("Android")
print("Operating System Type is", my_mobile.os_type)


def set_properties(obj, brand, name, cost):
    obj.brand_name = brand
    obj.model_name = name
    obj.price = cost


def get_properties(obj):
    return f"The brand is {obj.brand_name}, the model is  {obj.model_name}, the price is {obj.price}"


set_properties(my_laptop, "Dell", "Inspiron 432_15", 9800)
print(get_properties(my_laptop))

class Smartphone(Laptop):
    pass

my_smartphone = Smartphone()
set_properties(my_smartphone, "Samsung", "Galaxy S21 Ultra", 12000)
print(get_properties(my_smartphone))
# Inheritance in Python:
