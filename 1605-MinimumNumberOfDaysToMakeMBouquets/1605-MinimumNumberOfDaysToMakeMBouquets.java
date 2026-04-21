// Last updated: 4/21/2026, 11:24:25 PM
class Solution {
    public boolean possible(int[] bloomDay, int m, int k , int day){
        int cnt = 0;
        int b = 0;
        for(int i = 0; i < bloomDay.length; i++){
            if(bloomDay[i] <= day){
                cnt++;
            }
            else{
                b += (cnt/k);
                cnt = 0;
                }
        }
        b += (cnt/k);
        if(b >= m){
            return true;
        }
        else{
            return false;
        }
    }
    public int minDays(int[] bloomDay, int m, int k) {
     int high = Integer.MIN_VALUE;
     int low = 1;
     int ans  = -1;
     if( bloomDay.length < m*k ){
        return -1;
     }
     for(int i = 0; i< bloomDay.length; i++){
        high = Math.max(bloomDay[i], high);
    
     }   
     while(low <=high){
        int mid = low + (high - low)/2;
        if(possible(bloomDay, m, k , mid)){
            ans = mid;
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
     }
     return ans;
    }
}