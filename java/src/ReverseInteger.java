class Solution {
    public int reverse(int x) {
        int ans = 0, n = 0;

        do {
            n = x % 10;
            x /= 10;
            
            // overflow
            if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && n > 7)) return 0;
            if (ans < Integer.MIN_VALUE / 10 || (ans == Integer.MIN_VALUE / 10 && n < -8)) return 0;

            ans = ans * 10 + n;
        } while (x != 0);

        return ans;
    }
}