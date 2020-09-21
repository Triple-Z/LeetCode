class Solution {
    public boolean isValidBST(TreeNode root) {
        return recursive(root, null, null);
    }

    private boolean recursive(TreeNode node, Integer upper, Integer lower) {
        if (node == null) return true;
        
        if (upper != null && node.val >= upper) return false;
        if (lower != null && node.val <= lower) return false;

        return recursive(node.left, node.val, lower)
            && recursive(node.right, upper, node.val);
    }
}