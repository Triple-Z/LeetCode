class Solution {

    private Map<Integer, Integer> indexMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int n = inorder.length;

        // build in-order index mapping
        for (int i = 0; i < n; i++) {
            indexMap.put(inorder[i], i);
        }

        return recursive(preorder, inorder, 0, n - 1, 0, n - 1);
    }

    private TreeNode recursive(int[] preorder, int[] inorder, int preorderLeft, int preorderRight, int inorderLeft,
            int inorderRight) {
        if (preorderLeft > preorderRight)
            return null;

        int preorderRoot = preorderLeft;
        int inorderRoot = indexMap.get(preorder[preorderRoot]);

        // create the new root
        TreeNode root = new TreeNode(preorder[preorderRoot]);

        int leftSubTreeSize = inorderRoot - inorderLeft;

        root.left = recursive(preorder, inorder,
                // 先序遍历的左子树
                preorderRoot + 1, preorderLeft + leftSubTreeSize,
                // 中序遍历的左子树
                inorderLeft, inorderRoot - 1);

        root.right = recursive(preorder, inorder,
                // 先序遍历的右子树
                preorderLeft + leftSubTreeSize + 1, preorderRight,
                // 中序遍历的右子树
                inorderRoot + 1, inorderRight);

        return root;
    }
}