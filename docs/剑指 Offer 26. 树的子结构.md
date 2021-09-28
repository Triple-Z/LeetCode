<!-- omit in toc -->
# 剑指 Offer 26.  树的子结构

- Difficulty: Medium
- Topics: `Tree`, `Depth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Depth-First Search](#depth-first-search)
    - [Go](#go)

## Description

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
```
     3
    / \
   4   5
  / \
 1   2
```
给定的树 B：
```
   4 
  /
 1
```
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
```
输入：A = [1,2,3], B = [3,1]
输出：false
```
示例 2：
```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```
限制：

```
0 <= 节点个数 <= 10000
```

## Solution

### Depth-First Search

要查找树的子结构，肯定要对树进行遍历。那么首选的肯定是使用深度优先搜索对 A 进行遍历。

当遍历时找到了两棵树值为相同的“根”时，就要开始判断当前节点出发，B 树是否能跟当前 A 树的节点的子树相同。因此需要一个 `isSame(a, b)` 函数来判断子树是否相同。

在判断子树是否相同中，最值得注意的点就是若遍历到 B 树的节点为空时，则可返回 `true`，而不用去比较 A 树的子树中同样位置的节点是否也为空。

若 A 树当前节点的子树与 B 树不同，则需要继续查找 A 树的子树，因此还需要对左、右节点进行递归查找子结构。

若查找到了子结构，则返回 `true` ，否则继续查找。

#### Go

- 执行用时: 16 ms
- 内存消耗: 7 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubStructure(A *TreeNode, B *TreeNode) bool {
    if A == nil || B == nil {
        return false
    }

    if A.Val == B.Val && isSame(A, B) {
        return true
    }

    if isSubStructure(A.Left, B) {
        return true
    }

    if isSubStructure(A.Right, B) {
        return true
    }

    return false
}

func isSame(a *TreeNode, b *TreeNode) bool {
    if b == nil {
        return true
    }

    if a == nil {
        return false
    }

    if a.Val != b.Val {
        return false
    }

    return isSame(a.Left, b.Left) && isSame(a.Right, b.Right)
}
```

