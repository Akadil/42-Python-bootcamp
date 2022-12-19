# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 20:12:22 by akalimol          #+#    #+#              #
#    Updated: 2022/12/19 17:02:12 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from the_account import Account

class Bank:
    """
        My first bank
    """

    __accounts: list
    __name: str

    def __init__(self, name = "Tony Stark's bank"):
        self.__accounts = []
        self.__name = name

    def get_name(self):
        return self.__name

    def get_all_accounts(self):
        return self.__accounts

    def get_num_accounts(self):
        return len(self.__accounts)

    def __checkAccountType(self, account):
        """
            Check is the account is of right type
        """
        if type(account) is not Account:
            return False
        return True

    def __checkCorrupt(self, account):
        """
            This method check for the correctness of the bank
        """

        attrs = account.__dict__.keys()
        
        # Check "Even number of attributes"
        if len(attrs) % 2 == 0:
            print(f'Corrupted account! even number of attributes\n{attrs}')
            return False
        
        zip_check = 0 # Check "no attribute starting with zip or addr" (1/3)
        addr_check = 0 # Check "no attribute starting with zip or addr" (1/3)
        name_checker = ["__name", "__id", "__value"] # Check for "name, id, value" (1/3)

        # iterate through attributes
        for attr in attrs:
            # Check "Attributes starting for b"
            if str(attr)[0] == 'b':
                print("Corrupted account! attr starting with b")
                return False
            # Check "no attribute starting with zip or addr" (2/3)
            if str(attr).startswith("zip"):
                zip_check = 1
            if str(attr).startswith("addr"):
                addr_check = 1
            # Check for "name, id, value" (2/3)
            if str(attr)[8:] in name_checker:
                name_checker.remove(str(attr)[8:])

        # Check "no attribute starting with zip or addr" (3/3)
        if zip_check != 1 or addr_check != 1:
            print(f'Corrupted account! no attr starting with zip or addr {attrs}')
            return False

        # Check for "name, id, value" (3/3)
        if len(name_checker) != 0:
            print("Corrupted account! No name, id or value")
            return False

        # Check "name is string"
        if type(attrs["__name"]) is not str:
            print("Corrupted account! The name doesn't contain string")
            return False

        # Check "id is int"
        if type(attrs["__id"]) is not int:
            print("Corrupted account! The id is not int")
            return False

        if type(attrs["__value"]) is not int or type(attrs["value"]) is not float:
            print("Corrupted account! The value is not int or float")
            return False

        return True

    def transfer(self, origin, dest, amount):
        
        """" Perform the fund transfer
                @origin: str(name) of the first account
                @dest: str(name) of the destination account
                @amount: float(amount) amount to transfer
                @return True if success, False if an error occured
        """
        
        # Pseudocode:
        # -----------
        # 1. Check account existence
        # 2. Check account corruption
        # 3. Check the amount of money
        # 4. Make a transfer 

        # Get accounts from the base
        account_1 = None
        account_2 = None
        for account in self.__accounts:
            if account.get_name() == origin:
                account_1 = account
            if account.get_name() == dest:
                account_2 = account

        # Check for account existence
        if account_1 == None:
            print(f'Account {origin.get_name()} doesn\'t exist')
            return False
        if account_2 == None:
            print(f'Account {dest.get_name()} doesn\'t exist')
            return False

        # Check for corrupted accounts
        if self.__checkCorrupt(account_1) is False:
            print(f'The account {account_1.get_name()} is corrupted')
            return False
        if self.__checkCorrupt(account_2) is False:
            print(f'The account {account_2.get_name()} is corrupted')
            return False

        # Check the amount of money of dest account
        if account_1.get_value() < amount:
            print(f'The account {account_1.get_name()} doesn\'t have enough money')
            return False

        # Make the transfer of money
        account_1.transfer(-1 * amount)
        account_2.transfer(amount)

    def add(self, account):
        """ 
        Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """

        # Check for right attribute
        if self.__checkAccountType(account) is False:
            print("Wrong input was added. Provided account is not an account")
            return False

        # Check if account already exist
        if account in self.__accounts:
            print("Account already exist")
            return False

        self.__accounts.append(account)
        print("Successfully added!")
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """

        # Check the type of name
        if type(name) is not str:
            print(f'{name} is not a string')
            return False

        # Retrieve the account
        my_account = None
        for account in self.__accounts:
            if account.get_name() == name:
                my_account = account

        # Check for existence
        if my_account is None:
            print(f'The account {name} doesn\'t exist')
            return False

        print("Sorry man, can't do that")




















