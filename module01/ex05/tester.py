from the_account import Account
from the_bank import Bank

account_1 = Account("Akadil")
account_2 = Account("Noah")
account_1.transfer(1500)

my_bank = Bank()

my_bank.add(account_1)
my_bank.add(account_2)

print(my_bank.transfer("Akadil", "Noah", 750))
