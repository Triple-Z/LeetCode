class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) return 0;
        if (nums.length == 2) return nums[0] > nums[1] ? 0 : 1;
        return recursive(nums, 0, nums.length-1);
    }

    public int recursive(int[] nums, int left, int right) {
        if (left > right || left < 0 || right >= nums.length) return -1;
        int mid = left + (right - left) / 2;

        if (mid == 0) {
            if (nums[mid] > nums[mid+1]) return mid;
        } else if (mid == nums.length - 1 ) {
            if (nums[mid] > nums[mid-1]) return mid;
        } else {
            if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1])  {
                return mid;
            }
        }

        return Math.max(recursive(nums, left, mid-1), recursive(nums, mid+1, right));
    }
}