from cards import ClassicDeck, EmptyDeck, Card
from player import Player


class BlackJackGame:
    """
    The game class
    """

    deck: ClassicDeck
    dealers_hand: EmptyDeck

    def __init__(self,
                 player: Player,
                 decks: int = 4,
                 show_total_values: bool = False,
                 min_bet: int = 10):
        """
        Initializes the blackjack game
        """

        self.decks = decks
        self.player = player
        self.game_on = False
        self.show_total_values = show_total_values
        self.min_bet = min_bet
        self.bet = 0
        self.shuffle_at = 0.75
        self.table_width = 60

    def reset_decks(self):
        """
        Resets decks, some code is commented for testing purposes
        """

        if len(self.deck.cards) / (self.decks * ClassicDeck().cards_in_deck) <= self.shuffle_at:
            self.deck = ClassicDeck(decks=self.decks)
            self.deck.shuffle()

        self.dealers_hand = EmptyDeck()
        self.player.hands = [EmptyDeck()]

        # d = EmptyDeck()
        # d.add_card(self.deck.draw_card())
        # d.add_card(self.deck.draw_card())
        # self.player.hands = [d, d]

    def do_first_round(self):
        """
        Does the first round, gives 2 cards to the player (2 to each hand for the future)
        and 2 for the dealer, one of dealer's cards is faced down
        """

        for _ in range(2):
            for hand in self.player.hands:
                hand.add_card(self.deck.draw_card())
            self.dealers_hand.add_card(self.deck.draw_card())

        # """ ONE HAND ONLY """
        # self.player.hands[0].add_card(Card("♣", "2", 2))
        # self.player.hands[0].add_card(Card("♣", "A", 11))
        # self.dealers_hand.add_card(Card("♣", "6", 6))
        # self.dealers_hand.add_card(Card("♣", "A", 11))

        self.dealers_hand.cards[0].flip_face()

    def calc_hand_value(self, hand: EmptyDeck):
        """
        Calculates and returns a hand's total value
        """

        return sum([card.value for card in hand.cards if card.face_up])

    def get_hand_value_str(self, hand: EmptyDeck):
        """
        Converts the calculated value to a string and returns it
        """

        return f"({self.calc_hand_value(hand)})" if self.show_total_values else ""

    def print_table(self):
        """
        Prints the table
        """

        print("-" * self.table_width)
        print("Dealer's Hand".center(self.table_width))
        print((str(self.dealers_hand) + self.get_hand_value_str(self.dealers_hand)).center(self.table_width))
        print()
        print()
        print(("Bet: " + str(self.bet)).center(self.table_width))
        print()
        print()
        print(("Your Hand" + ("s" if len(self.player.hands) > 1 else "")).center(self.table_width))
        for hand in self.player.hands:
            print((str(hand) + self.get_hand_value_str(hand)).center(self.table_width))
        print(("Balance: " + str(self.player.balance)).center(self.table_width))
        print("-" * self.table_width)

    def set_bet_size(self):
        """
        Sets the bet size, while loop until the player gives the right amount
        """

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

    def bet_checking_balance(self):
        """
        Checks if it's possible to make a bet, asks if player wants to lower it when not enough funds,
        aborts if not possible to make a bet or player decides it
        """

        self.bet = self.player.get_bet(self.player.bet_size)
        if self.bet <= 0:
            if self.player.balance > self.min_bet:
                print("Balance:", self.player.balance, "- Bet size:", self.bet)
                inp = input("Balance's too low. Want to change bet size? ").strip().lower()
                print()
                if inp in ["y", "ye", "yes"]:
                    self.set_bet_size()
                    self.player.get_bet(self.bet)
                else:
                    print("Balance's too low. Can't play anymore.")
                    self.game_on = False
            else:
                print("Balance's too low. Can't play anymore.")
                self.game_on = False

    def print_help_codes(self):
        """
        Prints codes for player decisions during the game
        """

        print()
        print("Here are codes for player decisions:")
        print("s - Stand: You don't take any more cards and try to beat the dealer with the cards you got so far")
        print("h - Hit: You take one card, you still can take more cards if you don't bust")
        print("d - Double down: You take one last card and double your bet.")
        print("sur - Surrender: You lose half of your bet and continue to the next game immediately.")
        print("rules - Prompts to the rules help page")
        print("help - Prompts to this (codes) help page")
        print()

    def print_help_rules(self):
        """
        Prints rules for current blackjack game
        """

        print()
        print("The goal of the game is to beat the dealer. Cards have values, the closest to 21 wins.")
        print("If dealer and the player gets the same values for their cards, the game pushes to the next round.")
        print("Dealer must follow a strict set of rules, in this case always hit until 16 and stay on all 17's.")
        print("The values for the numbered cards are the same as the numbers themselves.")
        print("For all cards with pictures, the value is 10. For ace it's 11 or 1, player decides what suits best.")
        print("If the player gets an ace and any card valued 10 it's considered a blackjack, payout 3:2.")
        print("In all other player won situations player's initial bet is doubled.")
        print()

    def game_loop(self):
        """
        The game loop
        """

        # Sets up a couple things before staring the game
        self.game_on = True

        self.print_help_rules()
        self.print_help_codes()
        self.set_bet_size()
        self.deck = ClassicDeck(decks=self.decks)
        self.deck.shuffle()

        while self.game_on:
            # Checks if it's possible to make the bet, else aborts the game
            self.bet_checking_balance()
            if not self.game_on:
                break

            # Gives the initial cards to the player and dealer
            self.reset_decks()
            self.do_first_round()

            """ ONE HAND ONLY """
            # check for blackjack, also does push if dealer also gets a blackjack
            if self.calc_hand_value(self.player.hands[0]) == 21:
                self.dealers_hand.cards[0].flip_face()
                self.print_table()
                if self.calc_hand_value(self.dealers_hand) != 21:
                    self.player.fill_balance(int(self.bet * 2.5))
                    print(
                        f"You got a Blackjack! You won {int(self.bet * 1.5)}! Your new balance is {self.player.balance}")
                    # input("(Enter any key to start a new game) ")
                else:
                    self.player.fill_balance(self.bet)
                    print("Push")
                    # input("(Enter any key to start a new game) ")
                input("(Enter any key to start a new game) ")
                continue

            # Player's moves
            inp = ""
            surrendered = False
            while True:
                """ ONE HAND ONLY """
                # Temp solution, controls the values for when the player gets an ace
                if self.calc_hand_value(self.player.hands[0]) > 21:
                    for card in self.player.hands[0].cards:
                        if card.value == 11:
                            card.update_ace_value()
                            break
                    else:
                        break

                self.print_table()

                # Player's actions
                inp = input("> ").strip().lower()

                if inp == "s":          # Stand
                    break
                elif inp == "h":        # Hit
                    self.player.hands[0].add_card(self.deck.draw_card())
                elif inp == "d":        # Double down, checks for aces
                    self.player.fill_balance(self.bet)
                    self.bet = self.player.get_bet(self.bet * 2)
                    if self.bet > 0:
                        self.player.hands[0].add_card(self.deck.draw_card())
                        # check for ace:
                        if self.calc_hand_value(self.player.hands[0]) > 21:
                            for card in self.player.hands[0].cards:
                                if card.value == 11:
                                    card.update_ace_value()
                            else:
                                break
                        else:
                            break
                    else:
                        self.player.get_bet(self.player.bet_size)
                        print("Can't double down, balance too low")
                elif inp == "sur":      # Surrender
                    self.player.fill_balance(self.bet // 2)
                    print("You surrendered! Half of your bet was returned.")
                    surrendered = True
                    break
                elif inp == "rules":     # Prompts to the rules help page
                    self.print_help_rules()
                elif inp == "help":      # Prompts to the codes help page
                    self.print_help_codes()

            # Restarts the game if player surrenders
            if surrendered:
                continue

            # Check if player busts
            if self.calc_hand_value(self.player.hands[0]) > 21:
                self.print_table()
                print("You bussed")
                input("(Enter any key to start a new game) ")
                continue

            # Dealer's moves
            self.dealers_hand.cards[0].flip_face()
            self.print_table()
            while self.calc_hand_value(self.dealers_hand) < 17:

                # """ Soft 17 """
                # Currently not working well
                #
                # if self.calc_hand_value(self.dealers_hand) == 17:
                #     for card in self.dealers_hand.cards:
                #         if card.value == 11:
                #             card.update_ace_value()
                #             break
                #     else:
                #         break
                # elif self.calc_hand_value(self.dealers_hand) > 17:
                #     break

                self.dealers_hand.add_card(self.deck.draw_card())
                self.print_table()

            # Comparing Dealer's and Player's hands

            # Player wins
            if self.calc_hand_value(self.dealers_hand) > 21 or \
                    self.calc_hand_value(self.player.hands[0]) > self.calc_hand_value(self.dealers_hand):
                print("You won!")
                self.player.fill_balance(int(self.bet * 2))
            elif self.calc_hand_value(self.player.hands[0]) == self.calc_hand_value(self.dealers_hand):     # Push
                print("Push")
                self.player.fill_balance(self.bet)
            else:       # Player loses
                print("You lost")

            # Pause before starting a new game
            input("(Enter any key to start a new game) ")
