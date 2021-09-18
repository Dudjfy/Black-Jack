from cards import ClassicDeck, EmptyDeck


class Player:
    def __init__(self, deck: ClassicDeck, money: int):
        self.deck = deck
        self.hand = EmptyDeck()
        self.money = money

    def draw_cards(self, draw_amount: int = 1):
        for _ in range(draw_amount):
            self.hand.add_card(self.deck.draw_card())

    def print_hand(self):
        pass
