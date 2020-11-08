class Solution {
    Map<Integer, Integer> resMap = new HashMap<>();

    public int tribonacci(int n) {
        // terminator
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        if (resMap.containsKey(n)) return resMap.get(n);
        // current level logic
        // drill down
        int ans = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
        resMap.put(n, ans);
        return ans;
    }
}