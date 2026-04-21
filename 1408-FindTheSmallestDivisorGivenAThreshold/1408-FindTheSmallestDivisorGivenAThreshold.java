// Last updated: 4/21/2026, 11:24:32 PM
class Solution {
    // Function to check if a divisor works within the threshold
    public boolean isPossible(int[] nums, int div, int threshold) {
        int sum = 0;
        for (int num : nums) {
            sum += (num + div - 1) / div;  // This is equivalent to ceiling of num / div
        }
        return sum <= threshold;
    }
    
    public int smallestDivisor(int[] nums, int threshold) {
        int low = 1; 
        int high = Integer.MIN_VALUE;
        
        // Find the maximum number in the array
        for (int num : nums) {
            high = Math.max(num, high);
        }
        
        int ans = -1;
        // Perform binary search to find the smallest divisor
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isPossible(nums, mid, threshold)) {
                ans = mid;  // Save current divisor as answer
                high = mid - 1;  // Try for a smaller divisor
            } else {
                low = mid + 1;  // Try for a larger divisor
            }
        }
        
        return ans;  // Return the smallest valid divisor
    }
}
