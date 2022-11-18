from account import *
from pytest import *

class Test:
    def setup_method(self):
        self.a1 = Account('abdul')

    def test_init(self):
        assert self.a1.get_name() == 'abdul'
        assert self.a1.get_balance()== 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.deposit(0) is False
        assert self.a1.deposit(2) is True
        assert self.a1.get_balance() == 2
        assert self.a1.deposit(3.2) is True
        assert self.a1.get_balance() == approx(5.2, abs=0.001)

    def test_withdraw(self):
            assert self.a1.deposit(5) is True
            assert self.a1.withdraw(-3) is False
            assert self.a1.withdraw(0) is False
            assert self.a1.withdraw(2) is True
            assert self.a1.get_balance() == 3
            assert self.a1.withdraw(1.5) is True
            assert self.a1.get_balance() == approx(1.5, abs=0.001)

    def test_get_balance(self):
        assert self.a1.deposit(5)
        assert self.a1.withdraw(-3)
        assert self.a1.get_balance() == 2


    def test_get_name(self):
        assert self.a1.get_name() == 'abdul'