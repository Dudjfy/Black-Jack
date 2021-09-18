from cards import ClassicDeck
from player import Player

p = Player(ClassicDeck(print_columns=4, decks=1), 1000)

p.deck.shuffle()
p.draw_cards()

# p.hand.cards[0].flip_face()

print(p.deck, p.hand, p.money, sep="\n\n")
