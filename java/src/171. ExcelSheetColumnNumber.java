class Solution {
    public int titleToNumber(String s) {
        int sum = 0;
        int n = s.length();
        int w = 1;
        for (int i = n-1; i >= 0; i--, w *= 26) {
            int t = s.charAt(i) - 'A' + 1;
            sum += w * t;
        }

        return sum;
    }
}