# Last updated: 4/21/2026, 11:28:06 PM
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]  # Initialize with a valid sum

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target  # Found exact match

                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
