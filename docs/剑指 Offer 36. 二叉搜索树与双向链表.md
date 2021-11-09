<!-- omit in toc -->
# 剑指 Offer 36.  二叉搜索树与双向链表

- Difficulty: Medium
- Topics: `Stack`, `Tree`, `Depth-First Search`, `Binary Search Tree`, `Linked List`, `Binary Tree`, `Doubly-Linked List`
- Link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/

- [Description](#description)
- [Solution](#solution)
  - [In-order Traversal](#in-order-traversal)
    - [Java](#java)

## Description

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

![](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)


我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)


特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。


注意：本题与 [426 题](# "no ref") 相同。

## Solution

<!-- 见 [426 题题解](#Solution "no ref")。-->

### In-order Traversal


要把一颗二叉搜索树转换成排序的双向循环链表，对于「排序」，我们可以使用中序遍历二叉搜索树实现。而就地转置成循环链表，需要好好分析一下。

在中序遍历中，当遍历到根节点的时候，我们可以把整棵树分为三部分，分别是：左子树、根节点，以及右子树。根据二叉搜索树的性质，若要组成排序的链表，那么根节点的前一个节点一定是左子树的最右侧节点；同理，根节点的后一个节点一定是右子树最左侧节点，如下：

![offer_36](assets/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8/offer_36.jpg)


我们要实现的递归函数是一个输入为 根节点 和 当前链表末尾节点，输出为 组成新链表后链表末尾节点 。依据中序遍历，首先让左子树递归组成自己的子循环链表。到了根节点时，将根节点与左子树最后一个节点连接起来，并同时将当前的末尾节点设置为根节点，并将其传入右子树的递归函数中，返回右子树组合出来的链表末尾节点。

当递归完成后，链表如下所示：

![offer_36_list](assets/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8/offer_36_list.jpg)

距离完成我们还差最后一步：将头尾连接起来，形成一个双向循环链表。

由于上述过程已经获得了链表末尾节点，只要通过前序指针（左指针）即可获取到链表头节点。最后将两者连接即可。

此方法的时间复杂度为 O(n)，由于是就地转置，空间复杂度为 O(1)。

#### Java

- 执行用时: 0 ms
- 内存消耗: 37.5 MB

```java
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
```
