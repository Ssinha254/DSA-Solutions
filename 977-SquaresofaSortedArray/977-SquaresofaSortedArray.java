// Last updated: 8/20/2026, 5:10:37 PM
1class Solution {
2    public int[] sortedSquares(int[] nums) {
3        int neg = 0;
4        int pos = nums.length- 1;
5        int[] res = new int[nums.length];
6    
7        for(int i = nums.length- 1; i >= 0; i--){
8            if (Math.abs(nums[neg]) > Math.abs(nums[pos])){
9                res[i] = nums[neg] * nums[neg];
10                neg++;
11            }
12            else{
13                res[i] = nums[pos] * nums[pos];
14                pos--;
15            }
16        }
17        return res;
18
19    }
20}