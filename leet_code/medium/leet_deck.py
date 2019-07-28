class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        

        

        # 1) my original scuffed bubble sort solution that iterates through everything (worst)

        # sort the deck in ascending order
        # for i in range(len(deck)):
        #     for j in range(len(deck)):
        #         if j != len(deck) - 1:
        #             if deck[j] > deck[j+1]:
        #                 deck[j], deck[j+1] = deck[j+1], deck[j]
        
        # 2) actual bubble sort (average)

        for i in range(len(deck)):
            for j in range(len(deck)- 1 - i):
                if deck[j] > deck[j+1]:
                    deck[j], deck[j+1] = deck[j+1], deck[j]
        

        # 3) python's sorting method using timsort (best)

        # deck.sort()
        
        

        
        
        
        
        weird_deck = []


        for i in range(len(deck)):
            real_i = len(deck)- 1 - i
            if real_i == len(deck) - 1:
                weird_deck.append(deck[real_i])
            else:
                # insert the new number in front of the list
                weird_deck.insert(0, deck[real_i])
                # the last value of the list will be second in the list
                weird_deck.insert(1, weird_deck[len(weird_deck) - 1])
                # pop the duplicate value at the end of list
                weird_deck.pop()
                
    
        
        return weird_deck


#https://leetcode.com/problems/reveal-cards-in-increasing-order/