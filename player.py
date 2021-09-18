from cards import Deck


class Player:
    def __init__(self, deck: Deck, money: int):
        self.deck = deck
        self.hand = []
        self.money = money
