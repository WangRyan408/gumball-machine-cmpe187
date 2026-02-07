GUMBALLS = {
    'RED': 5,    # Red gumballs cost 5 cents (nickel)
    'YELLOW': 10  # Yellow gumballs cost 10 cents (dime)
}

class GumballMachine:
    def __init__(self):
        self.balance = 0  # Current balance in cents
        
    def insertCoin(self, coin_type: str) -> bool:
        """Insert a coin and update balance. Returns True if valid coin."""
        coin_type = coin_type.upper()
        
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
            print(f"Invalid coin '{coin_type}' returned.")
            return False
    
    def dispenseGumball(self, color: str) -> bool:
        """Dispense a gumball of specified color. Returns True if successful."""
        color = color.upper()
        
        if color not in GUMBALLS:
            print(f"Invalid gumball color: {color}")
            return False
        
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
    machine = GumballMachine()
    print("Welcome to the Gumball Vending Machine!")
    print("RED gumballs cost 5 cents (nickel)")
    print("YELLOW gumballs cost 10 cents (dime)")
    print("Valid coins: NICKEL, DIME, QUARTER")

    
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