from cards import ClassicDeck, EmptyDeck


class Player:
    """
    Player class
    """
    def __init__(self, balance: int):
        self.hands = [EmptyDeck()]
        self.balance = balance
        self.bet_size = 0

    def fill_balance(self, amount: int):
        """
        Fills balance
        """
        if amount > 0:
            self.balance += amount

    def get_bet(self, bet: int):
        """
        Gets bet if there is enough funds
        """
        if bet > 0 and self.balance - bet >= 0:
            self.balance -= bet
            return bet
        return 0
