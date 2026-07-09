class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Loops through the array and counts how many times each value is present
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Creates a new List where you have frequency, number pairs
        List<int[]> arr = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            arr.add(new int[] { entry.getValue(), entry.getKey() });
        }
        // Sort this list
        arr.sort((a, b) -> b[0] - a[0]);

        // Returns a list that contains the most frequent values until size is k
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = arr.get(i)[1];
        }
        return res;
    }
}
