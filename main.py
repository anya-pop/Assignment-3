class Account:
    _accountNumber = 0
    _accountHolderName = ''
    _rateOfinterest = 0
    _currentBalance = 4
    def __init__(self):
        pass
    def getAccountNumber(_accountNumber):
        return _accountNumber
    def getAccountHolderName(_accountHolderName):
        return _accountHolderName
    def getRateOfInterest(_rateOfinterest):
        return _rateOfinterest
    def getCurrentBalance(_currentBalance):
        return _currentBalance
    def deposit():
        pass
    def withdraw():
        pass
    
class SavingsAccount(Account):
    _minimumBalance = 0
    def __init__(self):
        pass
    def withdraw():
        pass

class ChequingAccount(Account):
    _overdraftAllowed = 0
    def withdraw():
        pass

class Bank(Account):
    _bankName = ''
    def openAccount():
        pass
    def SearchAccount():
        pass

class Program(Bank):
    def run():
        pass
    def ShowMainMenu():
        pass
    def ShowAccountMenu():
        pass