// Last updated: 8/20/2026, 10:58:48 PM
1class Solution {
2    public int removeDuplicates(int[] nums) {
3        int i = 2;
4        int k = 2;
5        while(i < nums.length){
6            nums[k] = nums[i];
7            if ( nums[i] == nums[k - 2]){
8                i++;
9            }
10            else{
11                i++;
12                k++;
13            }
14            
15
16        }
17        
18    return k;
19    
20   }
21}