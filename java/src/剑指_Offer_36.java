/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return null;
        }
        Node last = recursion(root, null);
        // find head
        Node head = last;
        while (head != null && head.left != null) {
            head = head.left;
        }
        
        head.left = last;
        last.right = head;

        return head;
    }

    private Node recursion(Node root, Node last) {
        if (root == null) {
            return last;
        }

        Node current = root;

        Node left = null;
        if (root.left != null) {
            last = recursion(root.left, last);   
        }
        current.left = last;
        
        if (last != null) {
            last.right = current;
        }
        // to here, LEFT_SUBTREE <-> curNode, and the curNode is the largest element in this doubly linked list.
        last = current;

        if (root.right != null) {
            last = recursion(root.right, last);
        }
        
        // return the RIGHT_SUBTREE last element
        return last;
    }
}