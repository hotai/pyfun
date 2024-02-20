import random
from card import Card

class Deck:
    def __init__(self):
        self.CARDS = []
        self.SUITS = ["spades", "clubs", "hearts", "diamonds"]
        self.RANKS = [
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
                {"rank": "A", "value": 11}
            ]

        for suit in self.SUITS:
            for rank in self.RANKS:
                self.CARDS.append(Card(suit, rank))

    def shuffle(self):
        if len(self.CARDS) < 2:
            return
        random.shuffle(self.CARDS)
        random.shuffle(self.CARDS)

    def deal(self, num):
        cards = []
        if len(self.CARDS) <= 0 or num < 1:
            return cards
        for n in range(num):
            cards.append(self.CARDS.pop())
        return cards
