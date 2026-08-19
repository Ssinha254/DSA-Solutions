// Last updated: 8/19/2026, 2:54:05 PM
1class Solution {
2    public int findDuplicate(int[] nums) {
3       int slow = 0;
4       int fast = 0;
5       while(fast < nums.length){
6         slow = nums[slow];
7         fast = nums[nums[fast]];
8         if(slow == fast){
9            break;
10        }
11       }
12        int slow2 = 0;
13        while (slow2 != fast){
14            slow2 = nums[slow2];
15            fast= nums[fast];
16        }
17        return slow2;
18       
19    }       
20}