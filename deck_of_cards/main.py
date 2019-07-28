from deck import Deck


deck = Deck()
print(deck)
deck.shuffle()
card1 = deck.deal_card()
print(card1)
print(deck)
hand = deck.deal_hand(100)
print(hand)
print(deck)
