// Last updated: 4/21/2026, 11:25:46 PM
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int[] hash = new int[n + 1];
        for(int i = 0; i < n ;i++){
            hash[nums[i]]+= 1;
        }
        int num = -1;
        for(int i = 0;i <= n;i++){
            if(hash[i] == 0){
                num = i;
            }
        }
        return num;
    }
}