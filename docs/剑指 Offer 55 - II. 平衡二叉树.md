<!-- omit in toc -->
# 剑指 Offer 55 - II.  平衡二叉树

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Top-Down Recursion](#top-down-recursion)
    - [Go](#go)
  - [Button-Up Recursion](#button-up-recursion)

## Description

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 `[3,9,20,null,null,15,7]`
```
    3
   / \
  9  20
    /  \
   15   7
```
返回 `true` 。

示例 2:

给定二叉树 `[1,2,2,3,3,null,null,4,4]`
```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```
返回 `false` 。

 

限制：
- 0 <= 树的结点个数 <= 10000


注意：本题与 [110 题](# "no ref") 相同。


## Solution

### Top-Down Recursion

要判断该树是不是平衡二叉树，首先要注意平衡二叉树的定义，即任意节点左右子树深度相差不超过 1。因此，我们可以借助在 剑指 Offer 55 - I 中实现的二叉树高度算法，计算出当前节点左右两子节点各自的深度，并判断当前节点的子树是否符合深度相差不超过 1 这一条件。若不符合，则说明该树肯定不是平衡二叉树，返回 `false` ；若符合，则继续遍历其子节点，待所有子节点都符合该条件，则为平衡二叉树。

该方法的时间复杂度为 O(n^2) ，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 5.7 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    if root == nil {
        return true
    }

    // pre-order
    leftHeight := height(root.Left)
    rightHegiht := height(root.Right)

    if leftHeight - rightHegiht > 1 || leftHeight - rightHegiht < -1 {
        return false
    }

    return isBalanced(root.Left) && isBalanced(root.Right)
}

func height(root *TreeNode) int {
    if root == nil {
        return 0
    }
    
    return max(height(root.Left), height(root.Right)) + 1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### Button-Up Recursion

TODO: 自底向上递归 https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/ping-heng-er-cha-shu-by-leetcode-solutio-6r1g/
