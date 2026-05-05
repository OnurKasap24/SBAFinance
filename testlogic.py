import unittest
from finance import income, expense, balance

class TestFinance(unittest.TestCase):

    def test_income(self):
        self.assertEqual(income(100), 100)

    def test_expense(self):
        self.assertEqual(expense(50), -50)

    def test_balance(self):
        self.assertEqual(balance([100, 200], [-50, -30]), 220)

if __name__ == "__main__":
    unittest.main()