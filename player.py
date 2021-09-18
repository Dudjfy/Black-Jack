from cards import Deck


class Player:
    def __init__(self, deck: Deck, money: int):
        self.deck = deck
        self.hand = []
        self.money = money

    def draw_card(self):
        self.hand.append(self.deck.cards[0])
        self.deck.cards.pop(0)

    def print_hand(self):
        pass
