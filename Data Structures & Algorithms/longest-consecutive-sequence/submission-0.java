class Solution {
    public int longestConsecutive(int[] nums) {

        if (nums.length == 0){
            return 0;
        } 
        if (nums.length == 1){
            return 1;
        }
        HashSet<Integer> seen = new HashSet<Integer>();
        for (int num: nums){
            seen.add(num);
        }

        int longest = 0;
        for (int num: seen){
            if (!(seen.contains(num - 1))){
                int current = 1;
                int currentNum = num;
                while (seen.contains(currentNum + 1)){
                    currentNum++;
                    current++;
                }
                if (current > longest){
                    longest = current;
                }
            }
        }
        return longest;
    }
}
