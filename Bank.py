class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    print("if you want to depost are withdraw then press the button ")
    choice = ("Deposit / withdraw")
    
    def deposit(self, amount):
        self.balance += amount
        print("Rs. ",amount,"deposit Successfully")
        print("And your current balance is ",self.balance)
        
    def withdraw(self,amount):
        if(amount > self.balance):
            print("Your current balance is not sufficient...")
        else:
            self.balance -= amount
            print("Rs. ",amount,"withdraw successfully")
            print("and your current balance is ",self.balance)
        
        
name = input("Pleas enter your name : ")
balance = int(input("Enter your current balance :"))
s1 = Bank(name,balance)

choice = input("enter youur choice depost / withdraw : ")
if(choice == "depost"):
    amount = int(input("Enter your desired amount for deposit : "))
    s1.deposit(amount)

elif(choice == "withdraw"):
    amount = int(input("Enter your desired amount for withdraw : "))
    s1.withdraw(amount)
else:
    print("Invalid choice")