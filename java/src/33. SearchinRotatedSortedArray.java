class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        if (n == 0)
            return -1;
        if (n == 1)
            return target == nums[0] ? 0 : -1;

        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (target == nums[mid])
                return mid;

            if (nums[left] <= nums[mid]) {
                // [left, mid] is in order.
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // [mid, right] is in order.
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        // `left` is greater than `right` after the while loop.

        return -1;
    }
}