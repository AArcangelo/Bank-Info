class account:

  def __init__(self,_name,_emailAddress,_phone_number,_city,_socialSecuritynumber,_isChecking):
    self.name = _name
    self.city = _city
    self.emailAddress = _emailAddress
    self.phone_number = _phone_number
    self.socialSecuritynumber = _socialSecuritynumber
    self.isChecking = _isChecking
    self.balance = 0

  def withdraw(self,withdrawamount):
    if self.balance- withdrawamount<0:
      return False
    else:
      self.balance-= withdrawamount
      return True 

  def deposit(self,depositamount):
    self.balance+= depositamount
    return True
  

  def check_balance(self):
   return self.balance












