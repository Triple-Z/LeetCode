class Solution {
    // pointers: [left, right)
    private int left = 0;
    private int right = 0;
    private int max = Integer.MIN_VALUE;
    private Map<Character, Integer> counters = new HashMap<>();

    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 1) return 0;

        while (right < s.length() && left <= right) {
            char cRight = s.charAt(right);
            char cLeft = s.charAt(left);
            if (!counters.containsKey(cRight)) {
                // move right
                counters.put(cRight, 1);
                right++;
            } else {
                // move left
                counters.remove(cLeft);
                left++;
            }

            // calc
            max = Math.max(max, right-left);
        }

        return max;
    }
}