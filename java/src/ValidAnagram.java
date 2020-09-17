class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> charMap = new HashMap<>();

        for (Character c : s.toCharArray()) {
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }

        for (Character c : t.toCharArray()) {
            charMap.put(c, charMap.getOrDefault(c, 0) - 1);
        }

        for (Character c : charMap.keySet()) {
            if (charMap.get(c) != 0) {
                return false;
            }
        }

        return true;
    }
}