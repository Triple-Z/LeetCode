<!-- omit in toc -->
# 剑指 Offer 54.  二叉搜索树的第k大节点

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

- [Description](#description)
- [Solution](#solution)
  - [In-order Traversal](#in-order-traversal)
    - [Go](#go)

## Description

给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
```
示例 2:
```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
```

限制：

1 ≤ k ≤ 二叉搜索树元素个数

## Solution

### In-order Traversal

由于该树是一颗二叉搜索树，有着左边节点都比根小、右边节点都比根大的性质，那么最大的值肯定是最右节点的值。要找到第 k 大节点，可以通过中序遍历（右-中-左），并辅以一个计数器来实现。

该题本质为在“反向”中序遍历的基础上增加迭代中共享的计数器，因此在迭代函数中需要将计数器的指针传入，并直接对该值进行操作。

#### Go

- 执行用时: 12 ms
- 内存消耗: 6.4 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargest(root *TreeNode, k int) int {
    if root == nil || k == 0 {
        return -1
    }

    return handler(root, &k).Val
}

func handler(root *TreeNode, k *int) *TreeNode {
    var target *TreeNode

    if root.Right != nil {
        target = handler(root.Right, k)
    }

    if target == nil {
        if *k == 1 {
            return root
        }
        *k--
    }

    if target == nil && root.Left != nil {
        target = handler(root.Left, k)
    }

    return target
}
```
