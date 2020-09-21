class Solution {
    public int maxDepth(TreeNode root) {
        // recursive
        if (root != null) {
            return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
        } else {
            return 0;
        }
    }
}
