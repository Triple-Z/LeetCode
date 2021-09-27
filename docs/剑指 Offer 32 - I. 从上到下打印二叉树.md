<!-- omit in toc -->
# 剑指 Offer 32 - I.  从上到下打印二叉树

- Difficulty: Medium
- Topics: `Tree`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Breadth-First Search](#breadth-first-search)
    - [Go](#go)

## Description

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


例如:
给定二叉树: `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```

返回：
```
[3,9,20,15,7]
```

提示：

1. `节点总数 <= 1000`

## Solution

### Breadth-First Search

使用队列来实现广度优先搜索，先将当前元素放入队列，再取出队头元素，将该元素值追加至结果，并将左右节点放入队列，循环直至队列为空。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.7 MB

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }

    queue := list.New()
    queue.PushBack(root)  // push
    ans := []int{}

    for queue.Len() > 0 {
        node := queue.Remove(queue.Front()).(*TreeNode)  // pop
        ans = append(ans, node.Val)
        if node.Left != nil {
            queue.PushBack(node.Left)  // push
        }
        if node.Right != nil {
            queue.PushBack(node.Right)  //push
        }
    }

    return ans
}
```
