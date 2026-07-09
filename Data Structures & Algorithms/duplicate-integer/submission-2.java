class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap dict = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (dict.containsValue(nums[i])){
                return true;
            }
            dict.put(i, nums[i]);
        }

        return false;
    }
}