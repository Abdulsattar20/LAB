class Account:
    def __init__(self, name:str):
        """
        this function create an account starting with name of account holder
        :param name: persons first name
        """
        self.__account_name = name
        self.__account_balance = 0



    def deposit(self, amount) -> bool:
        """
        this function recive the amount that wanted to be deposited
        :parm amount: amount of money that wanted to be deposited
        :return: if deposit succesful return true otherwise return false
        """
        if amount > 0 :
            self.__account_balance += amount
            return True
        else:
            return False



    def withdraw(self, amount:float)-> bool:
        """
        this function recive the amount that wanted to be withdrown from it
        :parm amount: amount of money that wanted to be withdrown
        :return: if transaction succesful return true otherwise return false
        """
        if amount>0 and amount<= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False



    def get_balance(self)-> float:
        """
        this function get the balance
        :return: toatal balance
        """
        return self.__account_balance




    def get_name(self)-> str:
        """
        this function get the  holder name
        :return: holder name
        """

        return self.__account_name







