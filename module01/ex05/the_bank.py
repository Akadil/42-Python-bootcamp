# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 20:12:22 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 21:02:45 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, ’value’):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str)
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank:

    """
    1. Check if it is the right object
    2. Chekc if it is corrupted
    3. Check if it stores enough information to make a transfer
    """
    ALL_ACCOUNTS = []
    
    name: str
    id: int
    value: float
    def __init__(self):





    # Check if the bank account is corrupted or not
    def checkCorrupt(self):
        attrs = self.__dict__.keys()
        
        # Check "Even number of attributes"
        if len(attrs) % 2 == 0:
            print("Corrupted account! even number of attributes")
            sys.exit()
        
        # Check "Attributes starting for b"
        for attr in attrs:
            if str(attr)[0] is 'b':
                print("Corrupted account! attr starting with b")
                sys.exit()

        # Check "no attribute starting with zip or addr"
        zip_check = 0
        addr_check = 0
        for attr in attrs:
            if str(attr).startswith("zip"):
                zip_check = 1
            if str(attr).startswith("addr"):
                addr_chekc = 1
        if zip_check != 1 or addr_check != 1:
            print("Corrupted account! no attr starting with zir or addr")
            sys.exit()

        # Check for "name, id, value"
        name_checker = ["name", "id", "value"]
        for attr in attrs:
            if str(attr) in name_checker:
                name_checker.remove(str(attr))
        if len(name_checker) != 0:
            print("Corrupted account! No name, id or value")
            sys.exit()

        # Check "name is string"
        if type(attrs["name"]) is not str:
            print("Corrupted account! The name doesn't contain string")
            sys.exit()

        # Check "id is int"
        if type(attrs["id"]) is not int:
            print("Corrupted account! The id is not int")
            sys.exit()

        if type(attrs["value"]) is not int or type(attrs["value"]) is not float:
            print("Corrupted account! The value is not int or float")
            sys.exit()

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
                @origin: str(name) of the first account
                @dest: str(name) of the destination account
                @amount: float(amount) amount to transfer
                @return True if success, False if an error occured
        """

    def checkTransfer(self, origin, dest, amount):
        # check for the validity of the accounts
        # Check the amount of the money, amount<0, or not enough

    def add(account):
        # Check for if the account with the same name exist in the database
        # Something like if not in ALL_ACCOUNTS, then add

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """





















