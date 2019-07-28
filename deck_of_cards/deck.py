from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, val) for val in values for suit in suits]
    
    def __repr__(self):
        return "Deck of " + str(len(self.cards)) + " cards"

    def _deal(self, num):
        if len(self.cards) == 0:
            raise ValueError('All cards have been dealt')

        if len(self.cards) > 1:
            if num > 1:
                i = 0 
                remove = []
                while i < num and len(self.cards) != 0:
                    remove.append(self.cards.pop())
                    i += 1
                return remove
            else:
                return self.cards.pop()
        else:
            return self.cards.pop()

    def count(self):
        return len(self.cards)
    
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
        else:
            raise ValueError('Only full decks can be shuffled')
    
    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, num):
        return self._deal(num)