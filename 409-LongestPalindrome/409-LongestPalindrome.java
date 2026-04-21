// Last updated: 4/21/2026, 11:25:34 PM
class Solution {
    public int longestPalindrome(String s) {
        int cnt = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length() ; i++){
            char key = s.charAt(i);
            map.put(key, map.getOrDefault(key, 0) + 1);
            if(map.get(key) % 2 == 0){
                cnt+=2;
            }
        }
        for(int i: map.values()){
            if(i % 2 == 1){
                cnt++;
                break;
            }
        }
        return cnt;
    }
}