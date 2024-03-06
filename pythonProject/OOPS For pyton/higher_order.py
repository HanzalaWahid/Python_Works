# assigned to varaible
def say_hello():
    print("hello")

my_func = say_hello
my_func()

# passed as arguments to other function
def greet(callback):
    callback()

def say_hi ():
    print("HI")

greet(say_hi)


# return from another function

def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


receiver = outer_function(4)
print(receiver(6))

def outer_function(x):
    def inner_funtion(y):
        return x + y

    return  inner_funtion

reciver = outer_function(8)
print(reciver(8))

