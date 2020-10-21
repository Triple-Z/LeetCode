class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ansMap = new HashMap<>();
        if (strs.length < 1) return new ArrayList<>();

        for (String curStr : strs) {
            char[] charArr = curStr.toCharArray();
            Arrays.sort(charArr);
            String sortedCurStr = Arrays.toString(charArr);
            if (!ansMap.containsKey(sortedCurStr)) {
                ansMap.put(sortedCurStr, new LinkedList<>());
            }
            ansMap.get(sortedCurStr).add(curStr);
        }

        return new ArrayList<>(ansMap.values());
    }
}