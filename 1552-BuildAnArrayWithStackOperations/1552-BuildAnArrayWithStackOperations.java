// Last updated: 4/21/2026, 11:24:26 PM
class Solution {
    public List<String> buildArray(int[] target, int n) {
      ArrayList<String> res = new ArrayList<>();
      int index = 0;
      for(int i = 1; i < n+1 ;i++){
        if(index == target.length){
            return res;
        }
        else if(target[index] == i){
            res.add("Push");
            index++;
        }
        else{
            res.add("Push");
            res.add("Pop");
            
        }
      }  
      return res;
    }
}
