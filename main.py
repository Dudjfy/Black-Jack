from cards import Deck
from cards import Card
from player import Player

p = Player(Deck(), 1000)

p.deck.shuffle()
p.draw_card()


print(p.deck, [str(card) for card in p.hand], p.money, sep="\n")
