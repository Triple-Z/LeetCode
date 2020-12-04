class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length < 1)
            return new int[] { -1, -1 };

        int first = binarySearchLeft(nums, target, 0, nums.length - 1);

        int last = -1;
        if (first != -1)
            last = binarySearchRight(nums, target, first, nums.length - 1);

        return new int[] { first, last };
    }

    private int binarySearchLeft(int[] nums, int target, int left, int right) {
        if (left >= right) {
            if (nums[left] == target)
                return left;
            else
                return -1;
        }

        // int mid = left + (right - left) / 2;
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target || nums[mid] > target)
            // go left
            return binarySearchLeft(nums, target, left, mid);

        // go right
        return binarySearchLeft(nums, target, mid + 1, right);
    }

    private int binarySearchRight(int[] nums, int target, int left, int right) {
        if (left >= right) {
            if (nums[right] == target)
                return right;
            else
                return -1;
        }

        // int mid = left + (right - left + 1) / 2;
        int mid = left + ((right - left + 1) >> 1);
        if (nums[mid] == target || nums[mid] < target)
            // go right
            return binarySearchRight(nums, target, mid, right);

        // go left
        return binarySearchRight(nums, target, left, mid - 1);
    }
}