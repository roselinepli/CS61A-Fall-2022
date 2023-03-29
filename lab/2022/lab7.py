class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return super().drive()


class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25)
    2
    >>> a.balance
    10
    >>> a.time_to_retire(11)
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        time, money = 0, self.balance
        while money < amount:
            money = money * (1 + self.interest)
            time += 1
        return time

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)
    'Insufficient funds'
    >>> ch.withdraw(3)
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3)
    7
    >>> ch.withdraw(3)
    5
    >>> ch.withdraw(5)
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            if amount > self.balance:
                self.free_withdrawals -= 1
                return "Insufficient funds"
            if amount > self.max_withdrawal:
                self.free_withdrawals -= 1
                return "Can't withdraw that amount"
            self.free_withdrawals -= 1
            self.balance = self.balance - amount
        else:
            if amount + self.withdraw_fee > self.balance:
                # self.free_withdrawals -= 1
                return "Insufficient funds"
            if amount + self.withdraw_fee > self.max_withdrawal:
                # self.free_withdrawals -= 1
                return "Can't withdraw that amount"
            self.balance = self.balance - amount - self.withdraw_fee
        return self.balance