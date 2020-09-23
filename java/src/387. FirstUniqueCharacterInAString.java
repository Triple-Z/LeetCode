class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> charMap = new HashMap<>();

        for (Character c : s.toCharArray()) {
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            Integer times = charMap.get(c);
            if (times != null && times == 1) {
                return i;
            }
        }
        
        return -1;
    }
}