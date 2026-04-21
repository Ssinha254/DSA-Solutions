// Last updated: 4/21/2026, 11:24:09 PM
class Solution {
    public int subarraySum(int[] nums) {
        int[] prefixSum = new int[nums.length];
        
        prefixSum[0] = nums[0];
        for(int i = 1; i < nums.length;i++){
            
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }
        int start, result = 0;
        for(int j = 0; j < nums.length; j++){
            start = Math.max(0, j - nums[j]);
            if(start == 0){
                result += prefixSum[j];
            }
            else{
                result += prefixSum[j] - prefixSum[start - 1];
             }
        }
        return result;
    }
}