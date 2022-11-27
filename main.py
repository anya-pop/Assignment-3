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
    def __init__(self, num, name, interest, balance, _minimumBalance = 1000):
        self._minimumBalance = _minimumBalance
        super().__init__(num, name, interest, balance)
    def withdraw(self, amount):
        self.balance = self.balance -amount
        while self.balance < 1000:
            amount = int(input("The amount you want to withdraw will bring your balance below minimum. Try again:"))
        print("Your balance is now:")
        return self.balance

class ChequingAccount(Account):
    _overdraftAllowed = 0
    def withdraw():
        pass

class Bank:
    _bankName = 'GWO'
    def SearchAccount(self, number):
        account1 = ChequingAccount(1234567, 'Anya', 4, 1020) #instances of the class Account
        account2 = SavingsAccount(2345678, 'Iman', 4, 3000)
        account3 = ChequingAccount(3456789, 'Aleks', 4, 300)
        account4 = SavingsAccount(4567890, 'Audrey', 4, 4000)
        account5 = SavingsAccount(5678901, 'Misha', 4, 4000)
        account6 = ChequingAccount(6789012, 'Ali', 4, 500)
        list = [account1, account2, account3, account4, account5, account6]                                #instances collected in a list for easier creation of the method SearchAccount
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
            account = account1
            print("This is Anya's chequing account\n")
            return account
        elif number == 2345678:
            print("This is Iman's savings account")
            account = account2
            return account
        elif number == 3456789:
            print("This is Aleks's chequing account")
            account = account3
            return account
        elif number == 4567890:
            print("This is Audrey's savings account")
            account = account4
            return account
        elif number == 5678901:
            print("This is Misha's savings account")
            account = account5
            return account
        elif number == 6789012:
            print("This is Ali's chequing account")
            account = account6
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
            elif mmchoice == "select account" or "s":
                number = int(input("Enter the number of the account you're looking for:"))
                #USES method from the bank class
                Program.ShowAccountMenu(banking.SearchAccount(number))
            else:
                print("\nInvalid option, try again.\nSelect Account / Exit\n")
    def ShowAccountMenu(account):
        print("This is your account menu. \nYou have the following options:") #presents account information/menu
        print("Check Balance - press 1\nDeposit - press 2\nWithdraw - press 3\nExit Account - press 4")
        while True:
            try:
                amchoice = input("Enter your option here:").lower()
            except:
                pass
            if amchoice != '1' and amchoice != '2' and amchoice != '3' and amchoice != '4':
                amchoice = input("Please only enter numbers from 1 to 4:")
            elif amchoice == '1':
                print("Your current balance is:")
                print(Account.getCurrentBalance(account))
            elif amchoice == '2':
                amount = int(input("You chose to deposit. Enter the amount:"))
                print(account.deposit(amount))
            elif amchoice == '3':
                amount = int(input("You chose to withdraw. Enter the amount:"))
                print(account.withdraw(amount))
            elif amchoice == '4':
                Program.ShowMainMenu()
    def run():
        Program.ShowMainMenu()

Program.run()
