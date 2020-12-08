class Solution {
    public int mySqrt(int x) {
        // binary search
        int left = 0, right = x / 2 + 1;
        
        while (left < right) {
            int mid = left + ((right - left + 1) >> 1);
            long square = (long) mid * mid;
            if (square > x) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }

        return left;
    }
}