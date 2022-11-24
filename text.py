class Account:
    def __init__(self, num, name, interest, balance, sav, chq):
        self.num = num
        self.name = name
        self.interest = interest
        self.balance = balance
        self.sav=sav
        self.chq=chq
    def getAccountNumber(self):
        return self.num
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
class Bank:
    _bankName = 'GWO'
    @classmethod
    def SearchAccount(self):
        anya = Account(1234567, 'Anya', 4, 1020,500,78) #instances of the class Account
        iman = Account(2345678, 'Iman', 4, (3000),(1200),32)
        aleks = Account(3456789, 'Aleks', 4, (300),(3000),34)
        audrey = Account(4567890, 'Audrey', 4, (4000),(3000),234)
        misha = Account(5678901, 'Misha', 4, (4000),(1000),34)
        ali = Account(6789012, 'Ali', 4, (500),(678),12)
        list = [anya, iman, aleks, audrey, misha, ali]                                #instances collected in a list for easier creation of the method SearchAccount
        number = input("Enter the number of the account you're looking for:")
        number = int(number)
        list2 = []
        for a in list:
            n = a.getAccountNumber()
            n = int(n)
            list2.append(n)
        print(list2)
        while number not in list2:
            print("This is not a correct number.")
            number = int(input("Try again:"))
        if number == 1234567:
            print("This is Anya's account")
        elif number == 2345678:
            print("This is Iman's account")
        elif number == 3456789:
            print("This is Aleks's account")
        elif number == 4567890:
            print("This is Audrey's account")
        elif number == 5678901:
            print("This is Misha's account")
        elif number == 6789012:
            print("This is Ali's account")
Bank.SearchAccount()