class bankaccount:
  def_init_self,account_number,account_holder_name,initial_balance=0.0):
self.__account_number=account_number
self.__account_holder_name=account_holder_name
self._account balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited ₹{}.new balance:₹{}".format(amount,self.__account_balance))         
    else:
      print("Invalid deposit amount.please deposit a positive amount.")
      def withdraw(self,amount):
        if amount>0:
          and amount<=self.__account_balance:
            self.__account_balance-=amount
            print("Withdrawn ₹{}.new balance:{}".format(amount,self.__account_balance))
          else:
            print("invalid withdrawl or Insufficient balance.")
          def display_balance(self):
            print("Account balance for{} (account{}):₹{}
.format(self._account_holder_name,self.account_number,self._account balance ))     
            acccount=bankaccount(account_number='12345',account_holder_name='pradeep',initial_balance=5000)
            account.display_balance()
            acccount.deposit(500)
            acccount.witdraw(200)