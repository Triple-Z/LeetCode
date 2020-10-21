class Solution {
    // pointers: [left, right)
    private int left = 0;
    private int right = 1;
    private int max = 1;
    private Map<Character, Integer> counters = new HashMap<>();

    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 1) return 0;
        counters.put(s.charAt(0), 1);

        while (right < s.length() && left < right) {
            char cRight = s.charAt(right);
            char cLeft = s.charAt(left);
            if (!counters.containsKey(cRight)) {
                // move right
                counters.put(cRight, 1);
                right++;
            } else if (right - left > 1) {
                // move left
                counters.remove(cLeft);
                left++;
            } else {
                // move left & right
                counters.remove(cLeft);
                counters.put(cRight, 1);
                left++; right++;
            }

            // calc
            max = Math.max(max, right-left);
        }

        return max;
    }
}