# Dictionary defining gumball types and their prices in cents
GUMBALLS = {
    'RED': 5,    # Red gumballs cost 5 cents (nickel)
    'YELLOW': 10  # Yellow gumballs cost 10 cents (dime)
}

"""
    A vending machine that dispenses red and yellow gumballs.
    The machine accepts nickels (5 cents), dimes (10 cents), and quarters (25 cents).
    Red gumballs cost 5 cents and yellow gumballs cost 10 cents.
    The machine tracks the customer's balance and returns change upon request.
    The machine provides a simple command-line interface for interaction.
"""

class GumballMachine:
    #Initializes the gumball machine with a balance of 0 cents.
    def __init__(self):
        self.balance = 0  # Current balance in cents customer inserted
        

        
        #Insert a coin into the machine and update the balance.
        #Args: coin_type: String representing the coin type ('NICKEL', 'DIME', or 'QUARTER')
        #Returns: bool: True if the coin was valid and accepted, False if invalid and returned
    def insertCoin(self, coin_type: str) -> bool: 
        coin_type = coin_type.upper()

        # Check coin type and add appropriate value to balance
        if coin_type == 'NICKEL':
            self.balance += 5
            print(f"Nickel accepted. Current balance: {self.balance} cents")
            return True
        elif coin_type == 'DIME':
            self.balance += 10
            print(f"Dime accepted. Current balance: {self.balance} cents")
            return True
        elif coin_type == 'QUARTER':
            self.balance += 25
            print(f"Quarter accepted. Current balance: {self.balance} cents")
            return True
        else:
            # Invalid coins are rejected and returned to customer
            print(f"Invalid coin '{coin_type}' returned.")
            return False
    


        #Dispense a gumball of specified color and update the balance.
        #Args: color: String representing the gumball color ('RED' or 'YELLOW')
        #Returns: bool: True if the gumball was successfully dispensed, False if not
    def dispenseGumball(self, color: str) -> bool:
        """Dispense a gumball of specified color. Returns True if successful."""
        color = color.upper()
        cost = GUMBALLS[color]
        if self.balance >= cost:
            self.balance -= cost
            print(f"{color} gumball dispensed! Remaining balance: {self.balance} cents")
            return True
        else:
            print(f"Insufficient funds. {color} gumball costs {cost} cents, you have {self.balance} cents.")
            return False
    

    def returnChange(self) -> int:
        """Return all remaining balance to customer."""
        change = self.balance
        if change > 0:
            print(f"Returning {change} cents in change.")
        else:
            print("No change to return.")
        self.balance = 0
        return change
    
    def getBalance(self) -> int:
        """Return current balance."""
        return self.balance


def main():
    """
    Main function that runs the interactive gumball vending machine interface.
    
    Provides a menu-driven interface allowing users to:
    - Insert coins
    - Dispense gumballs
    - Check balance
    - Return change
    - Exit the program
    """
    # Create a new gumball machine instance
    machine = GumballMachine()
    print("Welcome to the Gumball Vending Machine!")
    print("RED gumballs cost 5 cents (nickel)")
    print("YELLOW gumballs cost 10 cents (dime)")
    print("Valid coins: NICKEL, DIME, QUARTER")

     # Main interaction loop - continues until user chooses to exit
    while True:
        print("\nOptions:")
        print("1. Insert coin")
        print("2. Dispense RED gumball")
        print("3. Dispense YELLOW gumball")
        print("4. Return change")
        print("5. Check balance")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            coin = input("Enter coin type (NICKEL/DIME/QUARTER): ").strip()
            machine.insertCoin(coin)
            
        elif choice == '2':
            machine.dispenseGumball('RED')
            
        elif choice == '3':
            machine.dispenseGumball('YELLOW')
            
        elif choice == '4':
            machine.returnChange()
            
        elif choice == '5':
            print(f"Current balance: {machine.getBalance()} cents")
            
        elif choice == '6':
            if machine.getBalance() > 0:
                print(f"\nYou still have {machine.getBalance()} cents in the machine.")
                return_it = input("Return change before exiting? (yes/no): ").strip().lower()
                if return_it == 'yes':
                    machine.returnChange()
            print("\nThank you for using the Gumball Vending Machine!")
            break
            
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()