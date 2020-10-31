class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new LinkedList<>();
        if (root == null) return ans;

        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);

        ans.addAll(left);
        ans.add(root.val);
        ans.addAll(right);

        return ans;
    }
}