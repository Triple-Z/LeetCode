class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        int level = 1;

        if (root == null) return res;
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            List<Integer> curLevelList = new LinkedList<>();
            int curLevelSize = queue.size();
            for (int i = 0; i < curLevelSize; i++) {
                TreeNode curNode = queue.poll();
                if (curNode == null) continue;
                curLevelList.add(curNode.val);

                if (curNode.left != null) queue.offer(curNode.left);
                if (curNode.right != null) queue.offer(curNode.right);
            }
            res.add(curLevelList);
        }

        return res;
    }
}