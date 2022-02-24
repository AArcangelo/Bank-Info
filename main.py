from account import account
import json

accounts = []
currentAccount = None
def add_account():
  currentAccount = ""
  nameInput = input("Enter your name ")
  currentAccount+= "Name"+nameInput
  cityInput = input("Enter your City ")
  currentAccount+="City"+cityInput
  emailInput = input("Enter your Email Address ")
  currentAccount+= "Email Address"+emailInput
  socialInput = input("Enter your Social Security Number ")
  currentAccount+="Social Security Number"+socialInput
  numberInput = input("Enter your Phone Number ")
  currentAccount+= "Phone Number"+numberInput
  is_checking = input("Is this a Checking Account? ")
  currentAccount+= "Checking Account"+is_checking
  new_account = account(nameInput,cityInput,emailInput,socialInput,numberInput,is_checking)
  accounts.append(new_account)
  print(currentAccount)
  print(len(accounts))
  return mainMenu()

def load_account():
  global currentAccount
  nameInput = input("Enter your name")
  for account in accounts:
    if account.name == nameInput:
      currentAccount = account
      print (currentAccount)
      print("Account has been loaded")
      return mainMenu()
      

  print("An Account with that name doesn't exist")
  return mainMenu()

def withdraw():
  global currentAccount
  if currentAccount is None:
    print("There is no account found try again")
    return mainMenu()
  
  userInput = int(input("How much money do you want to withdraw?"))
  withdraw_result = currentAccount.withdraw(userInput)
  #print(withdraw_result)
  if withdraw_result is True:
    print("Withdraw was successful")
  else:
    print("Withdraw failed")
  return mainMenu()

def deposit():
  if currentAccount is None:
    print("There is no account found try again")
    return mainMenu()    
  Userinput = int(input("How much money do you want to deposit?"))
  deposit_result = currentAccount.deposit(Userinput)
  print(deposit_result)
  return mainMenu()
  

def checkBalance():
  print (currentAccount.check_balance())
  return mainMenu()
  

                  

  



def mainMenu():
  accountFile = open("accountInfo","r")
  accountData = accountFile.read()
  print("Welcome to April's ATM")
  userChoice = input("A-Add Account,B-Load Account,C-Withdraw,D-Deposit,E-Check Balance")
  if userChoice == "A":
     return add_account()
  elif userChoice == "B":
    return load_account()
  elif userChoice == "C":
    return withdraw()
  elif userChoice == "D":
    return deposit()
  elif userChoice == "E":
    return checkBalance()
  else:
    print("Error")
    return mainMenu()
  
mainMenu()





'''
deposit 
withdraw
transfer
stores accounts/create accounts
login/password
can't withdraw more than you have


Account Info:
Name(string)
City(string)
Email address(string)
Social Security Number(string and integer)
Phone Number(integer)

Is checking(boolean)
current balance(integer)

'''