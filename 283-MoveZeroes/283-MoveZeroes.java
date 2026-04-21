// Last updated: 4/21/2026, 11:25:43 PM
class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        for(int i = n - 1; i >= 0;i--){
            if(nums[i] == 0){
                for(int j = i; j < n - 1 ; j++){
                    nums[j] = nums[j+1];
                }
                nums[n-1] = 0;
            }
        }
    }
}