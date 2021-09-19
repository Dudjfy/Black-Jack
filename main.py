from blackJackGame import BlackJackGame
from player import Player

p = Player(1000)
bj = BlackJackGame(p, show_total_values=True)

bj.game_loop()
