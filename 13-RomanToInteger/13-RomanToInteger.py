# Last updated: 4/21/2026, 11:28:10 PM
class Solution:
    def romanToInt(self, s: str) -> int:
       nums = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
       num = 0
       for i in range(len(s) - 1,-1,-1):
        if i < len(s) - 1 and nums[s[i]] < nums[s[i + 1]]:
            num -= nums[s[i]]
        else:
            num += int(nums[s[i]]) 
            
       return num