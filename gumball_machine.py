GUMBALLS = {
    'RED': 5,
    'YELLOW': 10
}
COINS = ['QUARTER', 'DIME', 'NICKEL']

class GumballMachine:
    def __init__(self):
        # Amount of money owed by gumball
        self.redValue = 0
        self.yellowValue = 0

        # Internal state for money
        self.numPennies = 0
        self.numNickels = 0
        self.numDimes = 0
        self.numQuarters = 0
        self.numHalfDollars = 0
        self.numDollarCoins = 0
        self.nonUSCoins = 0

    def insertCoin(self, numPennies: int = 0, numNickels: int = 0, numDimes: int = 0, numQuarters: int = 0, numHalfDollars: int = 0, numDollarCoins: int = 0, nonUSCoins: int = 0) -> None:
        self.numPennies = numPennies
        self.numNickels = numNickels
        self.numDimes = numDimes
        self.numQuarters = numQuarters
        self.numHalfDollars = numHalfDollars
        self.numDollarCoins = numDollarCoins
        self.nonUSCoins = nonUSCoins
            
    def dispenseGumball(self, numRed: int, numYellow: int) -> None:
        self.redValue = GUMBALLS['RED'] * numRed
        self.yellowValue = GUMBALLS['YELLOW'] * numYellow

    def coinCheck(self):
        if (self.numPennies > 0):
            print(f"Invalid coins, returning {self.numPennies} pennies.\n")
            self.numPennies = 0
        if (self.numHalfDollars > 0):
            print(f"Invalid coin(s), returning {self.numHalfDollars} Half Dollar(s).\n")
        if (self.numDollarCoins > 0):
            print(f"Invalid coin(s), returning {self.numDollarCoins} Dollar Coin(s).\n")
        if (self.nonUSCoins > 0):
            print(f"Invalid coin(s), returning {self.nonUSCoins} Unknown Coin(s).\n")
            


    def returnChange(self) -> float:
        """
        Docstring for returnChange
        
        :param self: Description
        :return: Description
        :rtype: float
        """
        totalCost = self.redValue + self.yellowValue
        totalInserted = 