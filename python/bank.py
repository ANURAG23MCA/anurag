class BankAccount:
	def __init__(self,account_number,account_holder,account_type,balance=0):
		self.account_number=account_number
		self.account_holder=account_holder
		self.account_type=account_type
		self.balance=balance
	
	def deposit(self,amount):
		if amount>0:
			self.balance=self.balance+amount
			print("succesfull deposit of ",amount)
			print("new balance:",self.balance)
		else:
			print("invalid amount")
	
	def withdraw(self,amount):
		if 0<amount<=self.balance:
			self.balance=self.balance-amount
			print("succesfull withdraw")
			
			
		elif amount>self.balance:
			print("not possible to withdraw")
		else: 
			print("invalid")
	
	def get_balance(self):
		print("current balance=",self.balance)
		
account1=BankAccount("123","anurag","savings",1000)
print(account1.get_balance())

d_amount=int(input("enter deposit"))
print(account1.deposit(d_amount))
withdrawal_result =int(input("enter withdraw"))
print(account1.withdraw(withdrawal_result))
print(account1.get_balance())

