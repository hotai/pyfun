from card import Card

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calc_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += card.rank["value"]
            if card.rank["rank"] == "A":
                has_ace = True
        
        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        self.calc_value()
        return self.value

    def is_blackjack(self):
        return self.get_value == 21

    def show_hand(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for n, card in enumerate(self.cards):
            if n == 0 and self.dealer \
                and not show_all_dealer_cards \
                    and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()
