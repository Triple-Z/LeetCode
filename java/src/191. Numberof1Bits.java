public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        int tmp = n;
        
        for (int i = 0; i < 32; i++) {
            if ((tmp & 1) == 1) ans++;
            tmp = tmp >>> 1;
        }

        return ans;
    }
}