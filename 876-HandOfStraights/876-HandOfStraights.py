# Last updated: 4/21/2026, 11:24:55 PM
from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupsize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupsize != 0:
            return False

        hashmap = dict(Counter(hand))
        sorted_cards = sorted(hashmap.keys())
        for card in sorted_cards:
            if hashmap[card] > 0:
                count = hashmap[card]
                for i in range(groupsize):
                    if card + i not in hashmap or hashmap[card +i] < count:
                        return False
                    hashmap[card + i] -= count 
        return True