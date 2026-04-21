# Last updated: 4/21/2026, 11:24:15 PM
from collections import defaultdict
class DetectSquares(object):

    def __init__(self):
        self.hashmap = defaultdict(int)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.hashmap[(x,y)] += 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        X,Y = point
        counts = 0
        for (x,y) in self.hashmap:
            if X == x and y != Y:
                d = abs(y - Y)
                if (X + d, y)  in self.hashmap and (X + d,Y)  in  self.hashmap:
                    c1 = self.hashmap.get((X, y), 0)
                    c2 = self.hashmap.get((X + d, Y), 0)
                    c3 = self.hashmap.get((X + d, y), 0)

                    counts += c1 * c2 * c3
                if (X  - d, y)  in self.hashmap and (X - d, Y)  in  self.hashmap:
                    c1 = self.hashmap.get((X, y), 0)
                    c2 = self.hashmap.get((X - d, Y), 0)
                    c3 = self.hashmap.get((X - d, y), 0)

                    counts += c1 * c2 * c3
        return counts 



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)