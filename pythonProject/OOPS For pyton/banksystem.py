def logs(func):
    def wrapper(self,username,password,ammount):
        with open (f"{username}.txt","a") as fp:
            fp.write(f"Action: {func.__name__} , Ammount {ammount} \n ")
            return func (self,username,password,ammount)

class BankAccount:
    def __init__(self,username,password,balance):
        self.username = username
        self.password = password
        self.balance = balance

    def authentication(self,username,password):
        return self.username == username and self.password == password

    @logs
    def deposite(self,username,password,ammount):
        if self.authentication(username,password):
            if ammount > 0:
                self.balance += ammount
                print(f"Ammount deposite {ammount} , Total balance {self.balance}$")

            else:
                print("Transation  Deposite Invalid")
        else:
            print("Authentaction Invalid ")

    @logs
    def withdraw(self,username,password,ammount):
        if self.authentication(username,password):
            if ammount < self.balance:
                self.balance -= ammount
                print(f"Ammount Withdraw {ammount} ,Total balance {self.balance}$  ")
            else:
                print("Transation Invalid")
        else:
            print("Authentaction invalid")

account = BankAccount("Hanzala",'121',500)

username = input("Enter your name: ")
password = input("Enter your password: ")

account.deposite(username,password,700)
account.withdraw(username,password,450)
