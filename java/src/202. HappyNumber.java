class Solution {
    public boolean isHappy(int n) {
        int original = n;
        Set<Integer> s = new HashSet<>();
        s.add(n);
        while (n != 1) {
            int newN = 0;
            while (n != 0) {
                int t = n % 10;
                newN += t*t;
                n = n / 10;
            }
            if (newN == original) return false;
            if (s.contains(newN)) return false;
            s.add(newN);
            n = newN;
        }

        return true;
    }
}