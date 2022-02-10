from account import account

accounts = []
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




def mainMenu():
  print("Welcome to April's ATM")
  userChoice = input("A-Add Account,B-Load Account,C-Withdraw,D-Deposit,E-Check Balance")
  if userChoice == "A":
     return add_account()
  elif userChoice == "B":
    print("Load Account")
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