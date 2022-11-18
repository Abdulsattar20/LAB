class account


    def __init__(self, name:str):
        """
         this function gets the holder account name and a defult amount of 0

         """
        self.account_name = name
        self.account_balance = 0



    def deposit(self, amount: float)-> bool:
        """
         this function claculate the deposit amount to the total balance
         :return: if deposit succesful return true otherwise return false
         """
        if self.amount > 0 :
            self.accout_balance += self.amount
            return True
        else:
            return False



    def withdraw(self, amount:float)-> bool:
        """
        this function claculate the withdraw amount from the total balance
        :return: if transaction succesful return true otherwise return false
        """
        if self.amount>0 and self.account_balance>0:
            self.accout_balance -= self.amount
            return True
        else:
            return False



    def get_balance(self)-> float:
        """
        this function get the balance
        :return: toatal balance
        """
        return self.account_balance




    def get_name(self)-> str:
        """
        this function get the  holder name
        :return: holder name
        """

        return self.account_name







