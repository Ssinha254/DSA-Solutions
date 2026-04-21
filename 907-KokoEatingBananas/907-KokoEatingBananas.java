// Last updated: 4/21/2026, 11:24:48 PM
class Solution {

    public double calcHours(int[] piles, int k){
        double total =0;
        for(int i = 0; i < piles.length; i++){
            total += Math.ceil((double) (piles[i])/ (double) (k));
        }
        return total;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int high = Integer.MIN_VALUE;
        int low = 1;
        for(int i = 0; i < piles.length; i++){
            high = Math.max(piles[i], high);
        }
        while(low <= high){
            int mid = low + (high - low) / 2;
            double val = calcHours(piles, mid);
            if(val <= h){
                high = mid - 1;
                
            }
            else {
                low = mid + 1 ;
            }
            
        }
        return low;
    }
}