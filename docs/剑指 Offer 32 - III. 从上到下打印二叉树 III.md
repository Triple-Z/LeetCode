<!-- omit in toc -->
# 剑指 Offer 32 - III.  从上到下打印二叉树 III

- Difficulty: Medium
- Topics: `Tree`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Breadth-First Search](#breadth-first-search)
    - [Go](#go)
  - [Breadth-First Search and Reverse List](#breadth-first-search-and-reverse-list)
    - [Go](#go-1)

## Description

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。


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
  [20,9],
  [15,7]
]
```

提示：

- `节点总数 <= 1000`

## Solution

### Breadth-First Search

大框架仍然是广度优先遍历，但是题目中要求在偶数层遍历的顺序相反，我们可以在 [剑指 Offer 32 - II.  从上到下打印二叉树 II](./剑指%20Offer%2032%20-%20II.%20从上到下打印二叉树%20II.md) 的基础上，对每层中队列的方向做文章。

原先的队列一直是同向的，即元素从右侧进入、就会从左边弹出。

由于题目要求每层顺序刚好相反，那么我们可以使用以下规则来达成：
1. 当层数为奇数（ `level % 2 == 1`）：队列方向为**从右至左**（即对应 `list.List` 中的 `PushBack` 和 `Front`），且添加子节点的顺序为**先左节点后右节点**。
    ```
      -------------------
     <- ... <- Left <- Right
      -------------------
    ```
2. 当层数为偶数（ `level % 2 == 0`）：队列方向为**从左至右**（即对应 `list.List` 中的 `PushFront` 和 `Back`），且添加子节点的顺序为**先右节点后左节点**。
    ```
       -------------------
     Left -> Right -> ... ->
       -------------------
    ```

当队列没有元素时，则说明遍历完成，返回结果。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.8 MB

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

    ans := [][]int{}
    queue := list.New()
    queue.PushBack(root)
    level := 0

    for queue.Len() > 0 {
        curLevelNodes := queue.Len()
        level++
        nodeVals := []int{}
        for i := 0; i < curLevelNodes; i++ {
            if level % 2 == 1 {
                node := queue.Remove(queue.Front()).(*TreeNode)
                nodeVals = append(nodeVals, node.Val)

                if node.Left != nil {
                    queue.PushBack(node.Left)
                }
                if node.Right != nil {
                    queue.PushBack(node.Right)
                }
            } else {
                node := queue.Remove(queue.Back()).(*TreeNode)
                nodeVals = append(nodeVals, node.Val)

                if node.Right != nil {
                    queue.PushFront(node.Right)
                }
                if node.Left != nil {
                    queue.PushFront(node.Left)
                }
            }
        }
        ans = append(ans, nodeVals)
    }

    return ans
}
```

### Breadth-First Search and Reverse List

顺着 [剑指 Offer 32 - II.  从上到下打印二叉树 II](./剑指%20Offer%2032%20-%20II.%20从上到下打印二叉树%20II.md) 的思路，该题只是在偶数层上要求反向打印内容，那我们就可以先用 II 中的广度优先遍历方法，得到 II 中的结果数组，再对偶数层对应的数组进行翻转操作即可。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.8 MB

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

    ans := [][]int{}
    queue := list.New()
    queue.PushBack(root)

    for queue.Len() > 0 {
        curLevelNodes := queue.Len()
        nodeVals := make([]int, 0, curLevelNodes)
        for i := 0; i < curLevelNodes; i++ {
            node := queue.Remove(queue.Front()).(*TreeNode)
            nodeVals = append(nodeVals, node.Val)

            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
        }
        ans = append(ans, nodeVals)
    }

    for k := 0; k < len(ans); k++ {
        if k % 2 == 1 {
            // reverse list
            for i, j := 0, len(ans[k])-1; i < j; i, j = i+1, j-1 {
                ans[k][i], ans[k][j] = ans[k][j], ans[k][i]
            }
        }
    }

    return ans
}
```
