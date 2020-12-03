/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String ans = "";
        if (root == null) return ans;
        List<String> strList = new ArrayList<>();
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);
        
        while (!queue.isEmpty()) {
            TreeNode curNode = queue.removeFirst();
            if (curNode == null) {
                strList.add("null");
                continue;
            }
            strList.add(String.valueOf(curNode.val));
            
            queue.addLast(curNode.left);
            queue.addLast(curNode.right);
        }

        for (String str : strList) {
            ans += str + ",";
        }
        return ans.substring(0, ans.length()-1);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") return null;
        String[] dArr = data.split(",");
        int n = dArr.length;
        if (n < 1) return null;
        TreeNode root = new TreeNode(Integer.valueOf(dArr[0]));
        
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);

        int index = 0;
        while (!queue.isEmpty()) {
            TreeNode curNode = queue.removeFirst();
            if (++index >= n) break;
            String leftStr = dArr[index];
            String rightStr = dArr[++index];
            TreeNode leftNode = "null".equals(leftStr) ? null : new TreeNode(Integer.valueOf(leftStr));
            TreeNode rightNode = "null".equals(rightStr) ? null : new TreeNode(Integer.valueOf(rightStr));

            curNode.left = leftNode;
            curNode.right = rightNode;
            if (leftNode != null) queue.addLast(leftNode);
            if (rightNode != null) queue.addLast(rightNode);
        }
        
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));