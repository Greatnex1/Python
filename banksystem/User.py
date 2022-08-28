# a bank app using oop

class User():
    def __init__(self, name, age, gender, phoneNumber):
        self.name = name
        self.age = age
        self.gender = gender
        self.phoneNumber = phoneNumber

    def user_details(self):
        print("User Details :")
        print("------------------")
        print("Name : ", self.name, "\nAge : ", self.age, "\nGender : ", self.gender,
              "\nPhoneNumber : ", self.phoneNumber)
        print("------------------")

class Bank(User):
    def __init__(self, name, age, gender, phoneNumber):
        super().__init__(name, age, gender, phoneNumber)
        # self.amount = 0
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your present account balance is : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        # self.balance = self.balance - amount
        if self.amount > self.balance:
            print("Insufficient Funds, Balance Available is $ ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account Balance is : ", self.balance)

    def viewBalance(self):
        self.user_details()
        print("Your present account balance is : ", self.balance)
