class BankAccount:

  def __init__(self, name, age, checkings, savings, phoneNum, pw):
    self.name = name
    self.age=age
    self.checkings=checkings
    self.savings=savings
    self.phoneNum = phoneNum
    self.password = pw
  
acc1 = BankAccount('Joe', 50, 500000, 1910, 4081123812, 'apple')

acc2 = BankAccount('James',20, 100, 9, 4081928173, 'banana')
# acc3 = BankAccount('Iota', 30, 31197251, 1127738, 4082921181)
# acc4 = BankAccount('Jane', 32, 42000, 42001, 4089883615 )
# acc5 = BankAccount('Jonathan', 19, 89112, 71817, 4082981182)
# acc6 = BankAccount('Jimmy', 72, 1000200, 900, 4082293121 )



#whos account are we interacting with
verify = int(input("Please enter your phone number to verify your identity."))



  


#function to deposit or withdraw

def withdraw(self, amount):
  acc1.checkings -= amount
  print(f"Your balance is {acc1.checkings} in your checking account from {acc1.checkings+ amount}.")

def depCheck(self, amount):
  acc1.checkings += amount
  print(f"Your balance is {acc1.checkings} in your checking account {acc1.checkings- amount}.")

def depSav(self, amount):
  acc1.savings += amount
  print(f"Your balance is {acc1.savings} in your savings account {acc1.savings- amount}.")

  


  
which = 0
withordep = input("Do you want to withdraw or deposit?")
if withordep == 'withdraw':
  amount = int(input("How much would you like to withdraw?"))
  if amount > acc1.checkings:
    print("You can't withdraw more than you have in your account!")
    quit
  elif amount < acc1.checkings:
     withdraw('self', amount)
elif withordep == 'deposit':
  which = int(input("Enter 1 to deposit to checkings, 2 to deposit to savings"))
if which == 1:
  amount = int(input("How much would you like to deposit?"))
  depCheck('self', amount)
elif which ==2:
  amount = int(input("How much would you like to deposit?"))
  depSav('self', amount)
 
else:
  pass
