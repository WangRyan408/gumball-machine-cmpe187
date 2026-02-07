import unittest
from gumball_machine import GumballMachine


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

    def test_dispense_red_with_zero_balance(self):
        """
        Test Case 13: Dispense RED gumball with 0 balance
        Reason: Verify machine rejects dispensing when no coins inserted
        Input: dispenseGumball('RED') with balance = 0
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball('RED')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_yellow_with_zero_balance(self):
        """
        Test Case 14: Dispense YELLOW gumball with 0 balance
        Reason: Verify machine rejects dispensing when no coins inserted
        Input: dispenseGumball('YELLOW') with balance = 0
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball('YELLOW')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_yellow_with_insufficient_balance(self):
        """
        Test Case 15: Dispense YELLOW gumball with only 5 cents
        Reason: Verify machine rejects YELLOW (10c) when balance is only 5 cents
        Input: insertCoin('NICKEL'), dispenseGumball('YELLOW')
        Expected Output: return False, balance = 5 cents (unchanged)
        """
        self.machine.insertCoin('NICKEL')
        result = self.machine.dispenseGumball('YELLOW')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 5)

    def test_dispense_red_with_overpayment_quarter(self):
        """
        Test Case 16: Dispense RED gumball after inserting QUARTER
        Reason: Verify correct remaining balance after overpayment (25 - 5 = 20)
        Input: insertCoin('QUARTER'), dispenseGumball('RED')
        Expected Output: return True, balance = 20 cents
        """
        self.machine.insertCoin('QUARTER')
        result = self.machine.dispenseGumball('RED')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 20)

    def test_dispense_yellow_with_overpayment_quarter(self):
        """
        Test Case 17: Dispense YELLOW gumball after inserting QUARTER
        Reason: Verify correct remaining balance after overpayment (25 - 10 = 15)
        Input: insertCoin('QUARTER'), dispenseGumball('YELLOW')
        Expected Output: return True, balance = 15 cents
        """
        self.machine.insertCoin('QUARTER')
        result = self.machine.dispenseGumball('YELLOW')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 15)

    def test_dispense_red_with_overpayment_dime(self):
        """
        Test Case 18: Dispense RED gumball after inserting DIME
        Reason: Verify correct remaining balance (10 - 5 = 5)
        Input: insertCoin('DIME'), dispenseGumball('RED')
        Expected Output: return True, balance = 5 cents
        """
        self.machine.insertCoin('DIME')
        result = self.machine.dispenseGumball('RED')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 5)

    def test_dispense_two_red_gumballs(self):
        """
        Test Case 19: Dispense 2 RED gumballs after inserting DIME
        Reason: Verify sequential dispensing depletes balance correctly (10 - 5 - 5 = 0)
        Input: insertCoin('DIME'), dispenseGumball('RED'), dispenseGumball('RED')
        Expected Output: both return True, balance = 0 cents
        """
        self.machine.insertCoin('DIME')
        result1 = self.machine.dispenseGumball('RED')
        result2 = self.machine.dispenseGumball('RED')
        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_red_then_yellow(self):
        """
        Test Case 20: Dispense RED then YELLOW with 15 cents balance
        Reason: Verify mixed color dispensing in one session (15 - 5 - 10 = 0)
        Input: insertCoin('DIME'), insertCoin('NICKEL'), dispenseGumball('RED'), dispenseGumball('YELLOW')
        Expected Output: both return True, balance = 0 cents
        """
        self.machine.insertCoin('DIME')
        self.machine.insertCoin('NICKEL')
        result1 = self.machine.dispenseGumball('RED')
        result2 = self.machine.dispenseGumball('YELLOW')
        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_five_red_gumballs_from_quarter(self):
        """
        Test Case 21: Dispense 5 RED gumballs after inserting QUARTER
        Reason: Stress test — max gumballs from one coin (25 / 5 = 5)
        Input: insertCoin('QUARTER'), dispenseGumball('RED') x5
        Expected Output: all return True, balance = 0 cents
        """
        self.machine.insertCoin('QUARTER')
        for _ in range(5):
            result = self.machine.dispenseGumball('RED')
            self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_second_gumball_fails_insufficient_funds(self):
        """
        Test Case 22: First RED succeeds, second RED fails (only 5c inserted)
        Reason: Verify funds exhaustion mid-session blocks further dispensing
        Input: insertCoin('NICKEL'), dispenseGumball('RED'), dispenseGumball('RED')
        Expected Output: first True, second False, balance = 0 cents
        """
        self.machine.insertCoin('NICKEL')
        result1 = self.machine.dispenseGumball('RED')
        result2 = self.machine.dispenseGumball('RED')
        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_red_lowercase(self):
        """
        Test Case 23: Dispense gumball with lowercase color input
        Reason: Verify dispenseGumball handles case-insensitive color
        Input: insertCoin('NICKEL'), dispenseGumball('red')
        Expected Output: return True, balance = 0 cents
        """
        self.machine.insertCoin('NICKEL')
        result = self.machine.dispenseGumball('red')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_yellow_mixed_case(self):
        """
        Test Case 24: Dispense gumball with mixed case color input
        Reason: Verify dispenseGumball handles mixed case color
        Input: insertCoin('DIME'), dispenseGumball('Yellow')
        Expected Output: return True, balance = 0 cents
        """
        self.machine.insertCoin('DIME')
        result = self.machine.dispenseGumball('Yellow')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_invalid_color_blue(self):
        """
        Test Case 25: Dispense gumball with invalid color 'BLUE'
        Reason: Verify machine rejects invalid color gracefully
        Input: dispenseGumball('BLUE')
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball('BLUE')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_invalid_color_green(self):
        """
        Test Case 26: Dispense gumball with invalid color 'GREEN'
        Reason: Verify machine rejects another invalid color gracefully
        Input: dispenseGumball('GREEN')
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball('GREEN')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_empty_string_color(self):
        """
        Test Case 27: Dispense gumball with empty string color
        Reason: Verify machine rejects empty color input gracefully
        Input: dispenseGumball('')
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball('')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)


class TestReturnChange(TestGumballMachine):
    """Test cases for returning change functionality."""

    def test_return_change_with_positive_balance(self):
        """
        Test Case 28: Return change after inserting QUARTER
        Reason: Verify correct amount returned and balance reset to 0
        Input: insertCoin('QUARTER'), returnChange()
        Expected Output: returns 25, balance = 0 cents
        """
        self.machine.insertCoin('QUARTER')
        change = self.machine.returnChange()
        self.assertEqual(change, 25)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_return_change_with_zero_balance(self):
        """
        Test Case 29: Return change with 0 balance
        Reason: Verify no crash and returns 0 when nothing to return
        Input: returnChange() with balance = 0
        Expected Output: returns 0, balance = 0 cents
        """
        change = self.machine.returnChange()
        self.assertEqual(change, 0)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_return_change_after_partial_spend(self):
        """
        Test Case 30: Return change after partial spend
        Reason: Verify remaining balance returned after dispensing (25 - 5 = 20 returned)
        Input: insertCoin('QUARTER'), dispenseGumball('RED'), returnChange()
        Expected Output: returns 20, balance = 0 cents
        """
        self.machine.insertCoin('QUARTER')
        self.machine.dispenseGumball('RED')
        change = self.machine.returnChange()
        self.assertEqual(change, 20)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_double_return_change(self):
        """
        Test Case 31: Call returnChange twice in a row
        Reason: Verify second call returns 0 (idempotent after first return)
        Input: insertCoin('QUARTER'), returnChange(), returnChange()
        Expected Output: first returns 25, second returns 0
        """
        self.machine.insertCoin('QUARTER')
        first_change = self.machine.returnChange()
        second_change = self.machine.returnChange()
        self.assertEqual(first_change, 25)
        self.assertEqual(second_change, 0)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_return_change_after_exact_spend(self):
        """
        Test Case 32: Return change after spending exact amount
        Reason: Verify returns 0 when balance already depleted by dispensing
        Input: insertCoin('NICKEL'), dispenseGumball('RED'), returnChange()
        Expected Output: returns 0, balance = 0 cents
        """
        self.machine.insertCoin('NICKEL')
        self.machine.dispenseGumball('RED')
        change = self.machine.returnChange()
        self.assertEqual(change, 0)
        self.assertEqual(self.machine.getBalance(), 0)


class TestGetBalance(TestGumballMachine):
    """Test cases for balance checking functionality."""

    def test_initial_balance_is_zero(self):
        """
        Test Case 33: Verify initial balance is 0
        Reason: Constructor should set balance to 0
        Input: getBalance() on new machine
        Expected Output: 0
        """
        self.assertEqual(self.machine.getBalance(), 0)

    def test_balance_after_multiple_insertions(self):
        """
        Test Case 34: Verify balance after multiple coin insertions
        Reason: Balance must accurately reflect sum of all inserted coins
        Input: insertCoin('QUARTER'), insertCoin('DIME'), getBalance()
        Expected Output: 35 cents
        """
        self.machine.insertCoin('QUARTER')
        self.machine.insertCoin('DIME')
        self.assertEqual(self.machine.getBalance(), 35)

    def test_balance_is_idempotent(self):
        """
        Test Case 35: Call getBalance multiple times without state change
        Reason: getBalance should not mutate state — repeated calls return same value
        Input: insertCoin('DIME'), getBalance(), getBalance(), getBalance()
        Expected Output: all return 10
        """
        self.machine.insertCoin('DIME')
        balance1 = self.machine.getBalance()
        balance2 = self.machine.getBalance()
        balance3 = self.machine.getBalance()
        self.assertEqual(balance1, 10)
        self.assertEqual(balance2, 10)
        self.assertEqual(balance3, 10)


class TestFullWorkflow(TestGumballMachine):
    """Integration test cases covering end-to-end workflows."""

    def test_full_cycle_insert_dispense_return(self):
        """
        Test Case 36: Full cycle — insert, dispense, return change
        Reason: End-to-end happy path covering all operations
        Input: insertCoin('QUARTER'), dispenseGumball('RED'), returnChange()
        Expected Output: dispense True, change = 20, final balance = 0
        """
        self.machine.insertCoin('QUARTER')
        result = self.machine.dispenseGumball('RED')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 20)
        change = self.machine.returnChange()
        self.assertEqual(change, 20)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_fail_then_retry_after_inserting_more(self):
        """
        Test Case 37: Fail dispensing, insert more coins, then succeed
        Reason: Recovery workflow — user adds funds after failed attempt
        Input: dispenseGumball('YELLOW') [fails], insertCoin('DIME'), dispenseGumball('YELLOW')
        Expected Output: first False, second True, balance = 0
        """
        result1 = self.machine.dispenseGumball('YELLOW')
        self.assertFalse(result1)
        self.machine.insertCoin('DIME')
        result2 = self.machine.dispenseGumball('YELLOW')
        self.assertTrue(result2)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_multiple_dispense_then_return_remaining(self):
        """
        Test Case 38: Insert large amount, dispense multiple, return remaining
        Reason: Multi-dispense session with change return at the end
        Input: insertCoin('QUARTER'), insertCoin('QUARTER'), dispenseGumball('YELLOW'),
               dispenseGumball('RED'), returnChange()
        Expected Output: balance tracks 50 -> 40 -> 35, change = 35
        """
        self.machine.insertCoin('QUARTER')
        self.machine.insertCoin('QUARTER')
        self.assertEqual(self.machine.getBalance(), 50)
        self.machine.dispenseGumball('YELLOW')
        self.assertEqual(self.machine.getBalance(), 40)
        self.machine.dispenseGumball('RED')
        self.assertEqual(self.machine.getBalance(), 35)
        change = self.machine.returnChange()
        self.assertEqual(change, 35)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_after_returning_change(self):
        """
        Test Case 39: Try to dispense after returning all change
        Reason: Verify dispensing is blocked after funds returned
        Input: insertCoin('QUARTER'), returnChange(), dispenseGumball('RED')
        Expected Output: dispense returns False, balance = 0
        """
        self.machine.insertCoin('QUARTER')
        self.machine.returnChange()
        result = self.machine.dispenseGumball('RED')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)


class TestRobustness(TestGumballMachine):
    """Test cases for error handling and edge cases."""

    def test_insert_coin_none_returns_false(self):
        """
        Test Case 40: Insert None as coin type
        Reason: Verify machine rejects None input gracefully
        Input: insertCoin(None)
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.insertCoin(None)
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_dispense_gumball_none_returns_false(self):
        """
        Test Case 41: Dispense with None as color
        Reason: Verify machine rejects None input gracefully
        Input: dispenseGumball(None)
        Expected Output: return False, balance = 0 cents
        """
        result = self.machine.dispenseGumball(None)
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_insert_coin_with_whitespace(self):
        """
        Test Case 42: Insert coin with leading/trailing whitespace
        Reason: Verify machine accepts whitespace-padded input after stripping
        Input: insertCoin('  NICKEL  ')
        Expected Output: return True, balance = 5 cents (whitespace stripped)
        """
        result = self.machine.insertCoin('  NICKEL  ')
        self.assertTrue(result)
        self.assertEqual(self.machine.getBalance(), 5)

    def test_insert_numeric_string(self):
        """
        Test Case 43: Insert numeric string as coin
        Reason: Verify machine rejects numeric input
        Input: insertCoin('123')
        Expected Output: return False, balance = 0
        """
        result = self.machine.insertCoin('123')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)

    def test_insert_special_characters(self):
        """
        Test Case 44: Insert special characters as coin
        Reason: Verify machine rejects special character input
        Input: insertCoin('!@#$')
        Expected Output: return False, balance = 0
        """
        result = self.machine.insertCoin('!@#$')
        self.assertFalse(result)
        self.assertEqual(self.machine.getBalance(), 0)


if __name__ == '__main__':
    unittest.main()
