/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        recursive(root);
    }

    private TreeNode recursive(TreeNode root) {
        if (root == null) return null;

        TreeNode end = root;
        TreeNode tmp = root.right;
        root.right = root.left;
        root.left = null;
        TreeNode next = recursive(root.right);
        if (next == null) next = root;
        end = next;
        next.right = tmp;
        next = recursive(next.right);
        if (next == null) return end;
        end = next;

        return end;
    }
}