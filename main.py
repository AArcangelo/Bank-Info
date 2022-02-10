from account import account

accounts = []
currentAccount = None
def add_account():
  nameInput = input("Enter your name")
  cityInput = input("Enter your City")
  emailInput = input("Enter your Email Address")
  socialInput = input("Enter your Social Security Number")
  numberInput = input("Enter your Phone Number")
  is_checking = bool(input("Is this a Checking Account?"))
  new_account = account(nameInput,cityInput,emailInput,socialInput,numberInput,is_checking)
  accounts.append(new_account)
  print(len(accounts))
  return add_account()

def load_account():
  nameInput = input("Enter your name")
  for account in accounts:
    if account.name == nameInput:
      currentAccount = account
      return mainMenu()

  print("An Account with that name doesn't exist")
  return mainMenu()

def withdraw():
  userInput = int(input("How much money do you want to withdraw?"))
  withdraw_result = currentAccount.withdraw(userInput)
  print(withdraw_result)

  



def mainMenu():
  print("Welcome to April's ATM")
  userChoice = input("A-Add Account,B-Load Account,C-Withdraw,D-Deposit,E-Check Balance")
  if userChoice == "A":
     return add_account()
  elif userChoice == "B":
    return load_account()
  elif userChoice == "C":
    print("Withdraw")
  elif userChoice == "D":
    print("Deposit")
  elif userChoice == "E":
    print("Check Balance")
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