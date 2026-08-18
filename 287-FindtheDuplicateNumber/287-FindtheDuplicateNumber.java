// Last updated: 8/19/2026, 12:30:55 AM
1class Solution {
2    public int findDuplicate(int[] nums) {
3        HashMap<Integer, Integer> map = new HashMap<>();
4        for(int i = 0; i < nums.length; i++){
5            map.put(nums[i], 0);
6        }
7        for(int i = 0; i < nums.length; i++){
8            if (map.get(nums[i]) == 1){
9                return nums[i];
10            }
11            map.put(nums[i], map.get(nums[i]) + 1);
12        }
13    return 0;
14    }       
15}