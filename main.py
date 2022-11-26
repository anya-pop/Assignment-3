class Account:
    def __init__(self, num, name, interest, balance):
        self.num = num
        self.name = name
        self.interest = interest
        self.balance = balance
    def getAccountNumber(self):
        return self.num
    def getAccountHolderName(self):
        return self.name
    def getRateOfInterest(self):
        return self.interest
    def getCurrentBalance(self):
        return self.balance
    def deposit(self, amount):
        print("Your current balance is now:")
        self.balance = self.balance +amount
        return self.balance
    def withdraw(self, amount):
        print("Your current balance is now:")
        self.balance = self.balance -amount
        return self.balance


class SavingsAccount(Account): #as the savings and chequing account ARE types of account, inheritence is used.
    _minimumBalance = 0
    def withdraw():
        pass

class ChequingAccount(Account):
    _overdraftAllowed = 0
    def withdraw():
        pass

class Bank:
    _bankName = 'GWO'
    def SearchAccount(self, number):
        anya = Account(1234567, 'Anya', 4, 1020) #instances of the class Account
        iman = Account(2345678, 'Iman', 4, 3000)
        aleks = Account(3456789, 'Aleks', 4, 300)
        audrey = Account(4567890, 'Audrey', 4, 4000)
        misha = Account(5678901, 'Misha', 4, 4000)
        ali = Account(6789012, 'Ali', 4, 500)
        list = [anya, iman, aleks, audrey, misha, ali]                                #instances collected in a list for easier creation of the method SearchAccount
        list2 = []
        for a in list:
            n = a.getAccountNumber()
            n = int(n)
            list2.append(n)
        print(list2)
        while number not in list2: #ensures an account with this number exists
            print("This is not a correct number.")
            number = int(input("Try again:"))
        if number == 1234567:
            account = anya
            print("This is Anya's account")
            return account
        elif number == 2345678:
            print("This is Iman's account")
            account = iman
            return account
        elif number == 3456789:
            print("This is Aleks's account")
            account = aleks
            return account
        elif number == 4567890:
            print("This is Audrey's account")
            account = audrey
            return account
        elif number == 5678901:
            print("This is Misha's account")
            account = misha
            return account
        elif number == 6789012:
            print("This is Ali's account")
            account = ali
            return account
        

class Program:
    def ShowMainMenu():
        banking = Bank() #creating instance of the class bank  
        print("Welcome to GWO bank! \nYou have the following options:") #welcome message, shows the main menu
        print("Select Account\nExit")
        while True:
            try:
                mmchoice = input("Enter your option here:").lower()
            except: 
                pass
            if mmchoice == "exit":
               exit()
            elif mmchoice == "select account":
                number = int(input("Enter the number of the account you're looking for:"))
                #USES method from the bank class
                Program.ShowAccountMenu(banking.SearchAccount(number))
            else:
                print("\nInvalid option, try again.\nSelect Account / Exit\n")
    def ShowAccountMenu(account):
        print("This is your account menu. \nYou have the following options:") #presents account information/menu
        print("Check Balance - press 1\nDeposit - press 2\nWithdraw - press 3\nExit Account - press 4")
        amchoice = input("Enter your option here:").lower()
        while amchoice != '1' and amchoice != '2' and amchoice != '3' and amchoice != '4':
            amchoice = input("Please only enter numbers from 1 to 4:")
        if amchoice == '1':
            print("Your current balance is:")
            print(Account.getCurrentBalance(account))
        elif amchoice == '2':
            amount = int(input("You chose to deposit. Enter the amount:"))
            print(Account.deposit(account,amount))
        elif amchoice == '3':
            amount = int(input("You chose to withdraw. Enter the amount:"))
            print(Account.withdraw(account,amount))
        elif amchoice == '4':
            Program.ShowMainMenu()

    def run():
        Program.ShowMainMenu()

Program.run()
