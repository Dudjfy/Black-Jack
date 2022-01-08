import math
import random


# The card class
class Card:
    """
    A class to represent a card.

    Attributes
    ----------
    suit : str
        suit of the card
    symbol : str
        symbol of the card
    value : int
        black jack value of the card
    face_up: bool
        boolean value to see if the card is facing up or down

    Methods
    -------
    flip_face():
        Inverts the value of face_up.
    update_ace_value(additional=""):
        Updates card values if the card is an Ace (the symbol is an "A").
    """

    def __init__(self, suit: str, symbol: str, value: int, face_up=True):
        """
        Constructs all the necessary attributes for the card object. face_up is true by default.

        Parameters
        ----------
            suit : str
                suit of the card
            symbol : str
                symbol of the card
            value : int
                black jack value of the card
        """

        self.suit = suit
        self.symbol = symbol
        self.value = value
        self.face_up = face_up

    # Returns card's symbol and suit if faced up, otherwise returns card faced down
    def __str__(self):
        """
        Returns card's symbol and suit.

        If faced_up is true returns symbol and suit, otherwise returns a faced down card.

        Parameters
        ----------
            None

        Returns
        -------
            (str): String of the suit and symbol if faced up, otherwise a faced down card
        """

        return f"[{self.suit}{self.symbol:>2}]" if self.face_up else "[■■■]"

    # Flips cards face
    def flip_face(self):
        """
        Inverts the value of face_up.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """

        self.face_up = not self.face_up

    # Updates ace value
    def update_ace_value(self):
        """
        Updates card values if the card is an Ace (the symbol is an "A").

        Parameters
        ----------
            None

        Returns
        -------
            None
        """

        if self.symbol == "A":
            if self.value == 11:
                self.value = 1
            else:
                self.value = 11


# Empty Deck class, with suits and symbol-value pairs for creating new decks
class EmptyDeck:
    suits = ["♣", "♦", "♥", "♠"]
    symbols_and_values = {
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

    def __init__(self, print_columns: int = 8):
        self.print_columns = print_columns
        self.cards_in_deck = 52
        self.cards = []

    # Returns a string representation of the deck depending on the desired amount of columns
    def __str__(self):
        return self.get_deck_with_columns_str()

    # Makes the string to return for __str__
    def get_deck_with_columns_str(self):
        card_str = ""
        for i, card in enumerate(self.cards):
            card_str += str(card) + ("\n" if (i + 1) % self.print_columns == 0 else " ")
        return card_str

    # Draws a card if len is more than 0, for now may not work if the deck is empty
    # MAY FAIL RETURN
    def draw_card(self):
        if len(self.cards) > 0:
            card = self.cards[0]
            self.cards.pop(0)
            return card

    # Adds cards to the deck
    def add_card(self, card: Card):
        self.cards.append(card)

    # Shuffles the deck using random
    def shuffle(self):
        random.shuffle(self.cards)


# A classic deck subclass, creates the deck automatically upon initialization
class ClassicDeck(EmptyDeck):
    def __init__(self, print_columns: int = 8, decks: int = 1):
        super().__init__(print_columns)
        self.decks = decks

        self.create_deck(self.decks)

    # Creates the deck, with multiple decks at once if specified
    def create_deck(self, decks: int):
        for _ in range(self.decks):
            for suit in self.suits:
                for symbol, value in self.symbols_and_values.items():
                    self.cards.append(Card(suit, symbol, value))
