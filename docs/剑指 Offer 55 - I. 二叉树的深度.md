<!-- omit in toc -->
# 剑指 Offer 55 - I.  二叉树的深度

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Depth-First Search](#depth-first-search)
    - [Go](#go)
  - [Breadth-First Search](#breadth-first-search)
    - [Lang](#lang)

## Description

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 `[3,9,20,null,null,15,7]`，
```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度 3 。

 

提示：
- 节点总数 <= 10000


注意：本题与 [104 题](104.%20Maximum%20Depth%20of%20Binary%20Tree%20二叉树的最大深度.md) 相同。

## Solution

### Depth-First Search

树的最大深度为两子树的最大深度加上自身深度，因此可以使用深度优先搜索，终止条件则为当前节点为空，则深度为零。此方法时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 4 ms
- 内存消耗: 4.2 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### Breadth-First Search

TODO: BFS

#### Lang

```lang
2nd solution code goes here.
```
