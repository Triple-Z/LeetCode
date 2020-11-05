class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<List<Integer>>();
        }

        List<List<Integer>> ans = new LinkedList<>();

        // create a new queue
        LinkedList<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.addLast(root);
        nodeQueue.addLast(null);

        LinkedList<Integer> levelList = new LinkedList<>();
        boolean isOrderLeft = true;
        
        while (nodeQueue.size() > 0) {
            TreeNode curNode = nodeQueue.pollFirst();
            // using `null` to separate different levels
            if (curNode != null) {
                if (isOrderLeft) levelList.addLast(curNode.val);
                else levelList.addFirst(curNode.val);

                if (curNode.left != null) nodeQueue.addLast(curNode.left);
                if (curNode.right != null) nodeQueue.addLast(curNode.right);
            } else {
                // next level
                ans.add(levelList);
                levelList = new LinkedList<Integer>();
                // add delimiter
                if (nodeQueue.size() > 0) nodeQueue.addLast(null);
                // change order
                isOrderLeft = !isOrderLeft;
            }
        }

        return ans;
    }
}
