// Last updated: 4/21/2026, 11:26:35 PM
class Solution {
    public int findMin(int[] nums) {
        int high = nums.length - 1;
        int low = 0;
        int min= Integer.MAX_VALUE ;
        while( low <= high){
            int mid = low + (high - low)/2;
            
           
            if( nums[low]<= nums[mid]){
                    min = Math.min(nums[low], min);
                    low = mid + 1;
                }
            else{
                 min =  Math.min(nums[mid], min);
                 high = mid - 1 ;
            }
            
        }
        return min;
    
    }
}