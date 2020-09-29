public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int mask = 0b10000000000000000000000000000000;
        int ans = 0;
        int ansMask = 1;

        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) ans |= ansMask;
            mask >>>= 1;
            ansMask <<= 1;
        }

        return ans;
    }
}