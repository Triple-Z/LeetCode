class Solution {
    public int lengthOfLIS(int[] nums) {
        int maxLen = 0;
        if (nums.length == 0) return 0;
        if (nums.length == 1) return 1;

        // dp[i] = max(dp[j]) + 1
        // s.t. 0 <= j < i
        //      nums[j] < nums[i]

        int[] dp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }

        return maxLen;
    }
}