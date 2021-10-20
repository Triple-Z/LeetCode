<!-- omit in toc -->
# 剑指 Offer 68 - II.  二叉树的最近公共祖先

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Backtrack](#backtrack)
    - [Go](#go)
  - [Depth-First Search](#depth-first-search)
    - [Go](#go-1)

## Description

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  `root = [3,5,1,6,2,0,8,null,null,7,4]`


![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/binarytree.png)
 

示例 1:
```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```
示例 2:
```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
```

说明:

- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉树中。

注意：本题与 [236 题](# "no ref") 相同。


## Solution

### Backtrack

通过回溯的方法找出 `p` 和 `q` 的从 `root` 出发的路径，最终遍历两者路径，找到最后一个公共节点即可。

回溯方法的时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 8 ms
- 内存消耗: 7.7 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    pPath := findPath(root, p, []*TreeNode{})
    qPath := findPath(root, q, []*TreeNode{})

    var ans *TreeNode
    for i := 0; i < len(pPath) && i < len(qPath); i++ {
        if pPath[i] == qPath[i] {
            ans = pPath[i]
        } else {
            return ans
        }
    }

    return ans
}

func findPath(root, target *TreeNode, path []*TreeNode) []*TreeNode {
    if root == nil {
        return path
    }

    path = append(path, root)
    pathLen := len(path)

    if root != target {
        path = findPath(root.Left, target, path)
        if len(path) != pathLen {
            return path
        }
        path = findPath(root.Right, target, path)
        if len(path) != pathLen {
            return path
        }
        // backtrack
        path = path[:len(path)-1]
    }

    return path
}
```

### Depth-First Search

用递归的思想，也能顺利解决这个问题，首先先考虑函数退出条件：
1. 当前节点为空（`root == nil`），退出返回空。
2. 当前节点为 `p` 或 `q` ，退出返回当前节点。

然后递归获取到当前节点左子树和右子树中，对于 `p` 和 `q` 的最近公共祖先。

返回的值遵循以下条件：
- 从左子树获得的结果为空，则说明最近公共祖先位于右子树中，则返回右子树获得的结果。
- 从右子树获得的结果为空，则说明最近公共祖先位于左子树中，则返回左子树获得的结果。
- 若左右子树都有结果，则说明 `p` 和 `q` 刚好分布于当前节点两侧，最近公共祖先就为当前节点，返回当前节点。
- 若左右子树都没有结果，则说明 `p` 和 `q` 不存在于左右子树，返回空（即左右子树的任何一个结果）。

因此，我们能够将返回条件简化为：
- 若左右子树都有结果，则返回当前节点。
- 若左子树没有结果，则返回右子树的结果。
- 否则返回左子树的结果。

递归方法的时间复杂度为 O(n)，空间复杂度为 O(n)，与回溯方法相同，但是其能极大简化代码。

#### Go

- 执行用时: 8 ms
- 内存消耗: 7.6 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root == nil || root == p || root == q {
        return root
    }

    left := lowestCommonAncestor(root.Left, p, q)
    right := lowestCommonAncestor(root.Right, p, q)

    if left != nil && right != nil {
        return root
    } else if left == nil {
        return right
    }

    return left
}
```