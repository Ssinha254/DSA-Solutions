// Last updated: 8/20/2026, 10:25:40 PM
1class Solution {
2    public int removeDuplicates(int[] nums) {
3        int curr = 0;
4        int k = nums.length;
5        while(curr < k -2){
6            if (nums[curr + 2] == nums[curr]){
7                
8                int j = 0;
9                for (int i = curr+3; i < k; i++){
10                        nums[curr+2 +j] = nums[i];
11                        j++;
12                
13            } 
14            k -= 1;
15            }
16            else{
17            curr++;
18            }
19        
20    }
21    return k;
22    
23   }
24}