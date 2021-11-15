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
        if (root == null) {
            return "[]";
        }

        List<String> elements = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        while (queue.size() > 0) {
            TreeNode node = queue.poll();
            if (node.val == -1001) { // null value
                elements.add("null");
                continue;
            }

            if (node.left != null) {
                queue.add(node.left);
            } else {
                queue.add(new TreeNode(-1001));
            }

            if (node.right != null) {
                queue.add(node.right);
            } else {
                queue.add(new TreeNode(-1001));
            }

            elements.add(Integer.toString(node.val));
        }

        return "[" + String.join(",", elements) + "]";
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        // System.out.println(data);
        data = data.substring(1, data.length() - 1);
        String[] elements = data.split(",");

        if (elements.length < 3) {
            return null;
        }

        int rootVal = Integer.parseInt(elements[0]);
        TreeNode root = new TreeNode(rootVal);
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        
        for (int i = 1; i < elements.length; i = i + 2) {
            TreeNode parent = queue.poll();
            
            String left = elements[i];
            String right = elements[i + 1];

            if (!"null".equals(left)) {
                int leftVal = Integer.parseInt(left);
                TreeNode leftNode = new TreeNode(leftVal);
                parent.left = leftNode;
                queue.add(leftNode);
            }

            if (!"null".equals(right)) {
                int rightVal = Integer.parseInt(right);
                TreeNode rightNode = new TreeNode(rightVal);
                parent.right = rightNode;
                queue.add(rightNode);
            }
        }

        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));