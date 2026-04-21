// Last updated: 4/21/2026, 11:27:54 PM
class Solution {
    public int searchInsert(int[] nums, int target) {
        int high = nums.length - 1;
        int low = 0;
        int floor = nums.length;
        while(low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] >= target){
                floor = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return floor;
    }
}