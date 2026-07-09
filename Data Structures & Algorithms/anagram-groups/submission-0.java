class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> seen = new HashMap<>();
        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);
            seen.putIfAbsent(sortedS, new ArrayList<>());
            seen.get(sortedS).add(s);
        }
        return new ArrayList<>(seen.values());
    }
}
