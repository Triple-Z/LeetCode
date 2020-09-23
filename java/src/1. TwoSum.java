class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Brute force
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    int[] ret = {i, j};
                    return ret;
                }
            }
        }
        return null;
    }
}

class TwoSum {

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] expected = {2, 7};

        Solution solution = new Solution();
        int[] ret = solution.twoSum(nums, target);
        assert ret.equals(expected);
        System.out.println("Passed !");
    }
}