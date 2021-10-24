from blackJackGame import BlackJackGame
from player import Player

# Creates a player object with 10000 game currency
p = Player(10000)
# Creates the game object with player, sets some settings
bj = BlackJackGame(p, show_total_values=True)

# Starts the game loop
bj.game_loop()
