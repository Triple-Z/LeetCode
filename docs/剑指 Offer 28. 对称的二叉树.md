<!-- omit in toc -->
# 剑指 Offer 28.  对称的二叉树

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Depth-First Search](#depth-first-search)
    - [Go](#go)

## Description

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
但是下面这个 `[1,2,2,null,3,null,3]` 则不是镜像对称的:
```
    1
   / \
  2   2
   \   \
   3    3
```
 

示例 1：
```
输入：root = [1,2,2,3,4,4,3]
输出：true
```
示例 2：
```
输入：root = [1,2,2,null,3,null,3]
输出：false
```

限制：

- `0 <= 节点个数 <= 1000`


## Solution

### Depth-First Search

递归果然是最贴近人类直观思想的，不断递归比较左右两个子树及它们子树的值，最后的结果就能判断出是否为对称二叉树。

#### Go

判断两个指针都不为空，可以这样写，将三个条件缩减为两个（本质是除去两者都为空后，只需要或逻辑就涵盖两指针有一个为空的两种条件）：
```go
if left == nil && right == nil {
    return true
} else if left == nil || right == nil {
    return false
}
```

- 执行用时: 0 ms
- 内存消耗: 2.9 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    
    return recursion(root.Left, root.Right)
}

func recursion(left *TreeNode, right *TreeNode) bool {
    if left == nil && right == nil {
        return true
    } else if left == nil || right == nil {
        return false
    }

    if left.Val != right.Val {
        return false
    }

    return recursion(left.Left, right.Right) &&
            recursion(left.Right, right.Left)
}
```
