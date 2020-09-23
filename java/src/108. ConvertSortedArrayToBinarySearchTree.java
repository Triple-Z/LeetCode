class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return recursive(nums, 0, nums.length-1);
    }

    private TreeNode recursive(int[] nums, int left, int right) {
        if (left > right) return null;
        
        int mid = (right - left) / 2 + left;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = recursive(nums, left, mid-1);
        root.right = recursive(nums, mid+1, right);

        return root;
    }
}