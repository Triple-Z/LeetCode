<!-- omit in toc -->
# 剑指 Offer 32 - II.  从上到下打印二叉树 II

- Difficulty: Easy
- Topics: `Tree`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Breadth-First Search](#breadth-first-search)
    - [Go](#go)

## Description

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:

给定二叉树: `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：
```
[
  [3],
  [9,20],
  [15,7]
]
```

提示：
```
节点总数 <= 1000
```

## Solution

### Breadth-First Search

使用队列来实现 BFS 广度优先搜索。一共使用两层循环，外层则对队列大小进行判断，内层则对当前遍历层进行计数遍历（因为当前层的父节点肯定已经全部进入队列，在子节点推入队列前，应保存父节点个数，再计数遍历。这样就能够实现层次之间的区分。

#### Go

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
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }
    
    q := list.New()

    q.PushBack(root)

    ans := [][]int{}
    for q.Len() > 0 {
        level := []int{}
        curLen := q.Len()
        for i := 0; i < curLen; i++ {
            // pop out current level nodes
            node := q.Remove(q.Front()).(*TreeNode)
            level = append(level, node.Val)
            if node.Left != nil {
                q.PushBack(node.Left)
            }
            if node.Right != nil {
                q.PushBack(node.Right)
            }
        }
        ans = append(ans, level)
    }

    return ans
}
```
