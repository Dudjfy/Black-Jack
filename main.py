from cards import Deck
from cards import Card
from player import Player

p = Player(Deck(), 1000)

print(p.deck, p.hand, p.money)
