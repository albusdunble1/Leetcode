from card import Card
from deck import Deck
import unittest


class CardTest(unittest.TestCase):

    def setUp(self):
        self.card = Card('Diamonds', '2')
    
    def test_init(self):
        self.assertEqual(self.card.suit, 'Diamonds')
        self.assertEqual(self.card.value, '2')
        
    def test_repr(self):
        self.assertEqual(repr(self.card), "2 of Diamonds")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()