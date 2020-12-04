class Solution {
    public int hammingDistance(int x, int y) {
        // XOR
        int xor = x ^ y;

        // count 1
        int ans = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((xor & mask) != 0) ans++;
            mask <<= 1;
        }

        return ans;
    }
}