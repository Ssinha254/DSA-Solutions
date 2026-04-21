# Last updated: 4/21/2026, 11:24:57 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       return len(s) == len(goal) and goal in (s + s)