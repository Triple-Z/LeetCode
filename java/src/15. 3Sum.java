class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new LinkedList<>();
        int n = nums.length;

        Arrays.sort(nums);

        for (int i = 0; i < n-2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i-1] == nums[i]) continue;

            int target = -nums[i];
            int left = i+1, right = n-1;

            // two pointers
            while (left < right) {
                if (nums[left] + nums[right] == target) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++; right--;

                    while (left < right && nums[left] == nums[left-1]) left++;
                    while (left < right && nums[right] == nums[right+1]) right--;
                } else if (nums[left] + nums[right] < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return ans;

    }
}
