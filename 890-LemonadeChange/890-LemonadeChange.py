# Last updated: 4/21/2026, 11:24:50 PM
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10 and fives >= 1:
                tens += 1
                fives -=1
            elif bills[i] == 20:
                if tens >= 1 and fives >= 1 :
                    tens -= 1
                    fives -= 1 
                elif fives >= 3:
                    fives -=3
                else:
                    return False
            else:
                return False
        return True

