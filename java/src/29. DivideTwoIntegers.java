class Solution {
    public int divide(int dividend, int divisor) {
        // corner cases
        if (dividend == 0) return 0;
        if (divisor == 1) return dividend;

        int sign = 1;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)) {
            sign = -1;
        }
        long a = dividend;
        long b = divisor;
        if (a < 0) a = -a;
        if (b < 0) b = -b;
        long res = div(a, b);
        
        if (sign == 1) return res > (long) Integer.MAX_VALUE ? Integer.MAX_VALUE : (int) res;
        
        return (int) -res;
    }

    private long div(long a, long b) {
        if (a < b) return 0;
        long cnt = 1;
        long bExp = b;
        while ((bExp + bExp) <= a) {
            cnt += cnt; // double the count
            bExp += bExp; // double the bExp
        }

        return cnt + div(a - bExp, b);
    }
}