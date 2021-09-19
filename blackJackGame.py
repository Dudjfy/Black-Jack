from cards import ClassicDeck, EmptyDeck
from player import Player


class BlackJackGame:
    deck: ClassicDeck
    dealers_hand: EmptyDeck

    def __init__(self, player: Player, decks: int = 4, show_total_values: bool = False):
        self.decks = decks
        self.player = player
        self.game_on = False
        self.show_total_values = show_total_values

        self.player_moves = {
            "s": self.player_stand,
            "h": self.player_hit,
            "d": self.player_double,
            "sp": self.player_stand,
            "sur": self.player_stand,
        }

    def player_stand(self):
        pass

    def player_hit(self):
        self.player_hand.add_card(self.deck.draw_card())

    def player_double(self):
        self.player_hit()

    def reset_decks(self):
        self.deck = ClassicDeck(decks=self.decks)
        self.deck.shuffle()

        self.dealers_hand = EmptyDeck()
        self.player.hands = [EmptyDeck()]

    def do_first_round(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.draw_card())
            self.dealers_hand.add_card(self.deck.draw_card())
        self.dealers_hand.cards[0].flip_face()

    def calc_hand_value(self, hand: EmptyDeck):
        return sum([card.value for card in hand.cards if card.face_up])

    def get_hand_value_str(self, hand: EmptyDeck):
        return f"({self.calc_hand_value(hand)})" if self.show_total_values else ""

    def print_table(self, bet: int):
        width = 60

        print()
        print("Dealer's Hand".center(width))
        print((str(self.dealers_hand) + self.get_hand_value_str(self.dealers_hand)).center(width))
        print()
        print()
        print(("Bet: " + str(bet)).center(width))
        print()
        print()
        print("Your Hand".center(width))
        for hand in self.player.hands:
            print((str(hand) + self.get_hand_value_str(hand)).center(width))
        print(("Balance: " + str(self.player.balance)).center(width))
        print()

    def check_values(self):
        pass

    def game_loop(self):
        self.game_on = True

        while self.game_on:
            self.reset_decks()

            self.print_table(100)
            inp = input("> ")

            # Bet
            # print("Balance:", self.balance)
            # bet = int(input("Bet: "))
            # if self.balance - bet < 0:
            #     print("Can't bet that much!")
            #     continue
            # self.balance -= bet
            #
            # self.do_first_round()
            # self.print_table(bet)
            # inp = input('> ').strip().lower()
            # self.player_moves.get(inp, self.player_stand)()
            #
            # if inp == "s":
            #     self.dealers_hand.cards[0].flip_face()
            #     if self.calc_hand_value(self.player_hand) > 21:
            #         continue
            #
            #
            #     # self.print_table(bet)
            #
            #
            # inp = input('> ')
