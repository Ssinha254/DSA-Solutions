# Last updated: 4/21/2026, 11:28:12 PM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        area = 0
        while left <right:
            w = right - left
            h = min(height[left], height[right])
            area = max(area, w*h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area