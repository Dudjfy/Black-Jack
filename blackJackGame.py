from cards import ClassicDeck, EmptyDeck
from player import Player


class BlackJackGame:
    deck: ClassicDeck
    dealers_hand: EmptyDeck

    def __init__(self,
                 player: Player,
                 decks: int = 4,
                 show_total_values: bool = False,
                 min_bet: int = 10):

        self.decks = decks
        self.player = player
        self.game_on = False
        self.show_total_values = show_total_values
        self.min_bet = min_bet

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

        # d = EmptyDeck()
        # d.add_card(self.deck.draw_card())
        # d.add_card(self.deck.draw_card())
        # self.player.hands = [d, d]

    def do_first_round(self):
        for _ in range(2):
            for hand in self.player.hands:
                hand.add_card(self.deck.draw_card())
            self.dealers_hand.add_card(self.deck.draw_card())
        self.dealers_hand.cards[0].flip_face()

    def calc_hand_value(self, hand: EmptyDeck):
        return sum([card.value for card in hand.cards if card.face_up])

    def get_hand_value_str(self, hand: EmptyDeck):
        return f"({self.calc_hand_value(hand)})" if self.show_total_values else ""

    def print_table(self):
        width = 60

        print("-" * width)
        print("Dealer's Hand".center(width))
        print((str(self.dealers_hand) + self.get_hand_value_str(self.dealers_hand)).center(width))
        print()
        print()
        print(("Bet: " + str(self.player.bet_size)).center(width))
        print()
        print()
        print(("Your Hand" + ("s" if len(self.player.hands) > 1 else "")).center(width))
        for hand in self.player.hands:
            print((str(hand) + self.get_hand_value_str(hand)).center(width))
        print(("Balance: " + str(self.player.balance)).center(width))
        print("-" * width)

    def check_values(self):
        pass

    def set_bet_size(self):
        while True:
            print("Balance:", self.player.balance)
            inp = input(f"Set bet size (Min: {self.min_bet}): ").strip()
            if not inp.isdigit():
                print("Wrong value. Please try again.")
                print()
                continue

            self.player.bet_size = abs(int(inp))
            if self.player.get_bet(self.player.bet_size) <= 0:
                print("Wrong value. Please try again.")
                print()
                continue
            self.player.fill_balance(self.player.bet_size)
            break

    def bet(self):
        bet = self.player.get_bet(self.player.bet_size)
        if bet <= 0:
            if self.player.balance > self.min_bet:
                inp = input("Balance's too low. Want to change bet size? ").strip().lower()
                if inp in ["y", "ye", "yes", "j", "ja"]:
                    self.set_bet_size()
                    self.player.get_bet(self.player.bet_size)
                    return True
            else:
                print("Balance's too low. Can't play anymore.")
            return False
        return True

    def game_loop(self):
        self.game_on = True

        self.set_bet_size()

        while self.game_on:
            self.reset_decks()
            self.do_first_round()
            if not self.bet():
                break

            self.print_table()
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
