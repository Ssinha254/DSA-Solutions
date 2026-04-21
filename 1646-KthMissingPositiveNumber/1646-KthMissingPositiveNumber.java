// Last updated: 4/21/2026, 11:24:24 PM
class Solution {
    public int findKthPositive(int[] arr, int k) {
    int high = arr.length - 1;
    int low = 0;
    while(low <=high){
        int mid = (high + low)/2;
        int missing = arr[mid] - mid - 1;
        if(missing < k){
            low = mid + 1;
        } 
        else{
            high = mid - 1;
        }
    }
    return low + k;
        
    
    }
}