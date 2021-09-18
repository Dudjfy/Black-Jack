import random


class Deck:
    def __init__(self):
        self.cards_in_deck = 52
        self.suits = ["♣", "♦", "♥", "♠"]
        self.symbols_and_values = {
          "2": 2, 
          "3": 3, 
          "4": 4, 
          "5": 5, 
          "6": 6, 
          "7": 7, 
          "8": 8, 
          "9": 9, 
          "10": 10, 
          "J": 10, 
          "Q": 10, 
          "K": 10, 
          "A": 11
          }
    
        self.cards = []
        self.create_deck()
  
    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

    def create_deck(self):
        for suit in self.suits:
            for symbol, value in self.symbols_and_values.items():
                if symbol != 'A':
                    self.cards.append(Card(suit, symbol, value))
                else:
                    self.cards.append(Ace(suit, symbol, value))

    def shuffle(self):
        random.shuffle(self.cards)


class Card:
    def __init__(self, suit: str, symbol: str, value: int):
        self.suit = suit
        self.symbol = symbol
        self.value = value
  
    def __str__(self):
        return f"[{self.suit}{self.symbol:>2}]"

    def update_value(self):
        pass


class Ace(Card):
    def __init__(self, suit: str, symbol: str, value: int):
        super().__init__(suit, symbol, value)

    def update_value(self):
        if self.value == 11:
            self.value = 1
        else:
            self.value = 11
