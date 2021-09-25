<!-- omit in toc -->
# 剑指 Offer 27.  二叉树的镜像

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Depth-First Search](#depth-first-search)
    - [Go](#go)
  - [Breadth-First Search](#breadth-first-search)
    - [Lang](#lang)

## Description

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```
镜像输出：
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```
 

示例 1：
```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

限制：

- `0 <= 节点个数 <= 1000`

## Solution

### Depth-First Search

使用递归实现先序遍历，将左子树变为右子树的镜像，再将右子树变为左子树的镜像，先序遍历递归到底即可。

#### Go

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func mirrorTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }

    rootLeft := root.Left
    root.Left = mirrorTree(root.Right)
    root.Right = mirrorTree(rootLeft)

    return root
}
```

### Breadth-First Search

TODO: 用循环实现广度优先搜索

#### Lang

```lang
2nd solution code goes here.
```
