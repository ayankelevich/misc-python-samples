import datetime
import pytz

class Account:
    """ Simple account class with balance """
#  Class variable, applicable to all objects
    _power = "Electric"

#  Static method, no self reference. "_" - not an interface method
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

#   Kind of constructor, although apparently, there is new method
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    alex = Account("Alex", 0)
    alex.show_balance()

    alex.deposit(1000)
    # tim.show_balance()
    alex.withdraw(500)
    # tim.show_balance()

    alex.withdraw(2000)

    alex.show_transactions()

    print(alex._power)

    print(alex.__dict__)
    print(Account.__dict__)

'''Single Leading Underscore(_var): Naming convention indicating a name is meant for internal use. 
... Single Trailing Underscore(var_): Used by convention to avoid naming conflicts with Python keywords. 
Double Leading Underscore(__var): Triggers name mangling when used in a class context. _classname__var
Mangling is done to avoid conflicts with derived classes
Enforced by the Python interpreter.'''