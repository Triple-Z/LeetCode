class Solution {
    public int trailingZeroes(int n) {
        // count 5
        
        int powerOfFive = 5;
        int sum = 0;
        while (powerOfFive <= n) {
            sum += n / powerOfFive;
            powerOfFive *= 5;
        }
        
        return sum;
    }
}