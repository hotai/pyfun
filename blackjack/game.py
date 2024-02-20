from deck import Deck
from hand import Hand

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:    
            try:
                games_to_play = int(input("How many games to do you want to play? "))
            except:
                print("Please enter a number.")

        while game_number < games_to_play:
            game_number += 1
        
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.show_hand()
            dealer_hand.show_hand()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please enter 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["s", "stand", "h", "hit"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.show_hand()
            
            if self.check_winner(player_hand, dealer_hand):
                continue

            ph_value = player_hand.get_value()
            dh_value = dealer_hand.get_value()

            while dh_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dh_value = dealer_hand.get_value()
            
            dealer_hand.show_hand(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final game results")
            print("Your hand:", ph_value)
            print("Dealer's hand:", dh_value)

            self.check_winner(player_hand, dealer_hand, True)
        
        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins!")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You win!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            if player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")
            else:
                print("Dealer wins!")
            return True
        
        return False


