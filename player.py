from cards import ClassicDeck, EmptyDeck


class Player:
    def __init__(self, balance: int):
        self.hands = [EmptyDeck()]
        self.balance = balance

    def draw_cards(self, draw_amount: int = 1):
        for _ in range(draw_amount):
            self.hand.add_card(self.deck.draw_card())

    def print_hand(self):
        pass

    def bet(self, bet: int):
        if self.balance - bet >= 0:
            self.balance -= bet
            return bet
        return 0
