def logs(func):
    def wrapper(self, username, password, amount):
        with open(f"{username}.txt", "a") as fp:
            fp.write(f"Action: {func.__name__}, Amount: {amount}\n")
        return func(self, username, password, amount)
    return wrapper

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    @logs
    def deposit(self, username, password, amount):
        if self.authenticate(username, password):
            if amount > 0:
                self.balance += amount
                print(f"Deposit Amount is: {amount}. New balance is: {self.balance}")
            else:
                print("Invalid amount to deposit.")
        else:
            print("Authentication failed.")

    @logs
    def withdrawal(self, username, password, amount):
        if self.authenticate(username, password):
            if amount < self.balance:
                self.balance -= amount
                print(f"Withdrawal Amount is: {amount}. New balance is: {self.balance}")
            else:
                print("Invalid Amount to withdraw.")
        else:
            print("Authentication failed.")

account = BankAccount("hanzala", 123, 1500)

userName = input("Enter your userName: ")
password = input("Enter your password: ")

account.deposit(userName, password, 100)
account.withdrawal(userName, password, 600)









