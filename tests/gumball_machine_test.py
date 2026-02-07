import unittest
from gumball_machine import GumballMachine, GUMBALLS


class TestGumballMachine(unittest.TestCase):
    def setUp(self):
        self.machine = GumballMachine()

class TestCoinInsertion(TestGumballMachine):
    """Test cases for coin insertion functionality."""
    
    def test_insert_valid_nickel(self):
        """
        Test Case 1: Insert a valid nickel
        Reason: Verify machine accepts nickels and updates balance correctly
        Input: insertCoin('NICKEL')
        Expected Output: balance = 5 cents, return True
        """
        result = self.machine.insertCoin('NICKEL')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 5)

    def test_insert_valid_dime(self):
        """
        Test Case 2: Insert a valid dime
        Reason: Verify machine accepts dimes and updates balance correctly
        Input: insertCoin('DIME')
        Expected Output: balance = 10 cents, return True
        """
        result = self.machine.insertCoin('DIME')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 10)
    
    def test_insert_valid_quarter(self):
        """
        Test Case 3: Insert a valid quarter
        Reason: Verify machine accepts quarters and updates balance correctly
        Input: insertCoin('QUARTER')
        Expected Output: balance = 25 cents, return True
        """
        result = self.machine.insertCoin('QUARTER')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 25)
    
    def test_insert_multiple_coins(self):
        """
        Test Case 4: Insert multiple coins sequentially
        Reason: Verify balance accumulates correctly with multiple insertions
        Input: insertCoin('QUARTER'), insertCoin('DIME'), insertCoin('NICKEL')
        Expected Output: balance = 40 cents (25+10+5)
        """
        self.machine.insertCoin('QUARTER')
        self.machine.insertCoin('DIME')
        self.machine.insertCoin('NICKEL')
        self.assertEqual(self.machine.getBalance(), 40)
    
    def test_insert_invalid_penny(self):
        """
        Test Case 5: Insert an invalid coin (penny)
        Reason: Verify machine rejects pennies and doesn't update balance
        Input: insertCoin('PENNY')
        Expected Output: balance = 0 cents, return False
        """
        result = self.machine.insertCoin('PENNY')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)
    
    def test_insert_invalid_dollar(self):
        """
        Test Case 6: Insert an invalid coin (dollar)
        Reason: Verify machine rejects dollar bills and doesn't update balance
        Input: insertCoin('DOLLAR')
        Expected Output: balance = 0 cents, return False
        """
        result = self.machine.insertCoin('DOLLAR')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)
    
    def test_insert_case_insensitive_nickel(self):
        """
        Test Case 7: Insert coin with lowercase input
        Reason: Verify machine handles case-insensitive input
        Input: insertCoin('nickel')
        Expected Output: balance = 5 cents, return True
        """
        result = self.machine.insertCoin('nickel')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 5)
    
    def test_insert_case_insensitive_mixed(self):
        """
        Test Case 8: Insert coin with mixed case input
        Reason: Verify machine handles mixed case input
        Input: insertCoin('QuArTeR')
        Expected Output: balance = 25 cents, return True
        """
        result = self.machine.insertCoin('QuArTeR')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 25)
    
    def test_insert_empty_string(self):
        """
        Test Case 9: Insert empty string as coin
        Reason: Verify machine handles invalid empty input gracefully
        Input: insertCoin('')
        Expected Output: balance = 0 cents, return False
        """
        result = self.machine.insertCoin('')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)
    
    def test_insert_random_string(self):
        """
        Test Case 10: Insert random invalid string
        Reason: Verify machine rejects arbitrary invalid input
        Input: insertCoin('Pound')
        Expected Output: balance = 0 cents, return False
        """
        result = self.machine.insertCoin('Pound')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

        
class TestGumballDispensing(TestGumballMachine):
    """Test cases for gumball dispensing functionality."""

    def test_dispense_red_gumball_with_exact_balance(self):
        """
        Test Case 11: Dispense RED gumball with exact balance
        Reason: Verify machine dispenses a RED gumball and updates balance correctly
        Input: insertCoin('NICKEL'), dispenseGumball('RED')
        Expected Output: return True, balance = 0 cents
        """
        self.machine.insertCoin('NICKEL')
        result = self.machine.dispenseGumball('RED')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_yellow_gumball_with_exact_balance(self):
        """
        Test Case 12: Dispense YELLOW gumball with exact balance
        Reason: Verify machine dispenses a YELLOW gumball and updates balance correctly
        Input: insertCoin('DIME'), dispenseGumball('YELLOW')
        Expected Output: return True, balance = 0 cents
        """
        self.machine.insertCoin('DIME')
        result = self.machine.dispenseGumball('YELLOW')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 0)
