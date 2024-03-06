def log(func):
    def wrapper(self,ammount):
        func(self,ammount)
        with open ("file.txt","a+") as fp:
            fp.write(f"Ammount {ammount} {func.__name__} succesfully")
    return wrapper

class BankAccount:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.balance = 0
        self.isAuth =False

    def Auth(self,username,password):
        if self.username == username and self.password == password:
            self.isAuth = True
        else:
            self.isAuth = False

    @log
    def deposite(self,ammount):
        if self.isAuth:
            if ammount > 0:
                self.balance += ammount
    @log
    def withdraw(self,ammount):
        if self.isAuth:
            if ammount < self.balance:
                self.balance -= ammount
            else:
                print("Invalid transcation")

acc = BankAccount("abc","2")
acc.Auth("abc","2")
acc.deposite(400)
acc.withdraw(100)
