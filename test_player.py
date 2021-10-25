import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.p = Player(1000)

    def test_balance_1000(self):
        self.assertEqual(self.p.balance, 1000)

    def test_fill_negative(self):
        self.p.fill_balance(-100)
        self.assertEqual(self.p.balance, 1000)

    def test_fill_zero(self):
        self.p.fill_balance(0)
        self.assertEqual(self.p.balance, 1000)

    def test_fill_100(self):
        self.p.fill_balance(100)
        self.assertEqual(self.p.balance, 1100)

    def test_return_get_bet_negative(self):
        bet = self.p.get_bet(-100)
        self.assertEqual(bet, 0)

    def test_balance_get_bet_negative(self):
        self.p.get_bet(-100)
        self.assertEqual(self.p.balance, 1000)

    def test_return_get_bet_zero(self):
        bet = self.p.get_bet(0)
        self.assertEqual(bet, 0)

    def test_balance_get_bet_zero(self):
        self.p.get_bet(0)
        self.assertEqual(self.p.balance, 1000)

    def test_return_get_bet_100(self):
        bet = self.p.get_bet(100)
        self.assertEqual(bet, 100)

    def test_balance_get_bet_100(self):
        self.p.get_bet(100)
        self.assertEqual(self.p.balance, 900)

    def test_return_get_bet_with_more_funds_than_balance(self):
        bet = self.p.get_bet(10000)
        self.assertEqual(bet, 0)

    def test_balance_get_bet_with_more_funds_than_balance(self):
        self.p.get_bet(10000)
        self.assertEqual(self.p.balance, 1000)


if __name__ == '__main__':
    unittest.main()