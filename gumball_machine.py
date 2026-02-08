# Gumball prices in cents
GUMBALLS = {
    'RED': 5,
    'YELLOW': 10
}

class GumballMachine:
    """Simple gumball vending machine that accepts nickels, dimes, and quarters."""
    
    def __init__(self):
        self.balance = 0
    
    def insertCoin(self, coin_type: str) -> bool:
        """Add a coin to the machine. Returns True if accepted."""
        if not isinstance(coin_type, str):
            print("Invalid input. Please insert a valid coin.")
            return False
        
        coin_type = coin_type.strip().upper()

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
        """Try to dispense a gumball. Returns True if successful."""
        if not isinstance(color, str):
            print("Invalid input. Please select a valid gumball color.")
            return False
        
        color = color.strip().upper()
        
        if color not in GUMBALLS:
            print(f"Invalid color '{color}'. Available colors: {', '.join(GUMBALLS.keys())}")
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
        """Give back any remaining balance."""
        change = self.balance
        if change > 0:
            print(f"Returning {change} cents in change.")
        else:
            print("No change to return.")
        self.balance = 0
        return change
    
    def getBalance(self) -> int:
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
            print("Invalid choice. `lease enter 1-6.")


if __name__ == "__main__":
    main()