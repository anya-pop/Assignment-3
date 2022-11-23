import site
class Account:
    def __init__(self, num, name, interest, balance, sav, chq):
        self.num = num
        self.name = name
        self.interest = interest
        self.balance = balance
        self.sav=sav
        self.chq=chq
    def getAccountNumber(num):
        return num
    def getAccountHolderName(name):
        return name
    def getRateOfInterest(interest):
        return interest
    def getCurrentBalance(balance):
        return balance
    def deposit():
        pass
    def withdraw():
        pass


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
    def names():
        anya = Account(1234567, 'Anya', 4, SavingsAccount(1020),ChequingAccount(500)) #instances of the class Account
        iman = Account(2345678, 'Iman', 4, SavingsAccount(3000),ChequingAccount(1200))
        aleks = Account(3456789, 'Aleks', 4, SavingsAccount(300),ChequingAccount(3000))
        audrey = Account(4567890, 'Audrey', 4, SavingsAccount(4000),ChequingAccount(3000))
        misha = Account(5678901, 'Misha', 4, SavingsAccount(4000),ChequingAccount(1000))
        ali = Account(6789012, 'Ali', 4, SavingsAccount(500),ChequingAccount(678))
        list = [anya, iman, aleks, audrey, misha, ali] #instances collected in a list for easier creation of the method SearchAccount
    def SearchAccount(self):
        number = input("Enter the number of the account you're looking for:")
        

class Program:
    def ShowMainMenu():
        banking = Bank()
        print("Welcome to GWO bank! \nYou have the following options:") #welcome message, shows the main menu
        print("Select Account\nExit")
        mmchoice = input("Enter your option here:").lower()
        if mmchoice == "exit":
            exit()
        else:
            banking.SearchAccount() #USES method from the bank class
    def ShowAccountMenu():
        print("This is your account menu. \nYou have the following options:") #presents account information/menu
        print("Check Balance - press 1\nDeposit - press 2\nWithdraw - press 3\nExit Account - press 4")
        amchoice = input("Enter your option here:").lower()
        while amchoice != '1' and amchoice != '2' and amchoice != '3' and amchoice != '4':
            amchoice = input("Please only enter numbers from 1 to 4:")
        if amchoice == '1':
            Account.getCurrentBalance()
        elif amchoice == '2':
            Account.deposit()
        elif amchoice == '3':
            Account.withdraw()
        elif amchoice == '4':
            Program.ShowMainMenu()
    @classmethod #decorator to call the method easier
    def run():
        Program.ShowMainMenu()

Program.ShowMainMenu()
