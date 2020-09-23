class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return recursive(root.left, root.right);
    }

    private boolean recursive(TreeNode left, TreeNode right) {
        if (left == null && right == null) return true;
        if (left != null && right != null) {
            if (left.val != right.val) return false;
            return recursive(left.right, right.left)
                && recursive(left.left, right.right);
        }
        return false;
    }
}