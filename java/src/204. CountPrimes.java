class Solution {
    public int countPrimes(int n) {
        if (n < 3) return 0;

        int count = 1; // just 2
        for (int i = 3; i < n; i++) {
            if ((i & 1) == 0) continue; // can be mod with 2
            boolean prime = true;
            for (int j = 3; j*j <= i; j+=2) { // j <= sqrt(i)
                if (i % j == 0) {
                    prime = false;
                    break;
                }
            }
            if (prime) count++;
        }

        return count;
    }
}
