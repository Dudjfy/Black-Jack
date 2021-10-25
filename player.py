from cards import ClassicDeck, EmptyDeck


# Player class
class Player:
    def __init__(self, balance: int):
        self.hands = [EmptyDeck()]
        self.balance = balance
        self.bet_size = 0

    # Fills balance
    def fill_balance(self, amount: int):
        if amount > 0:
            self.balance += amount

    # Gets bet if there is enough funds
    def get_bet(self, bet: int):
        if bet > 0 and self.balance - bet >= 0:
            self.balance -= bet
            return bet
        return 0
