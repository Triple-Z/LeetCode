<!-- omit in toc -->
# 剑指 Offer 33.  二叉搜索树的后序遍历序列

- Difficulty: Medium
- Topics: `Stack`, `Tree`, `Binary Search Tree`, `Recursion`, `Binary Tree`, `Monotonic Stack`
- Link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Recursion](#recursion)
    - [Go](#go)
  - [Monotonic Stack](#monotonic-stack)

## Description

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 `true`，否则返回 `false`。假设输入的数组的任意两个数字都互不相同。


参考以下这颗二叉搜索树：
```
     5
    / \
   2   6
  / \
 1   3
```
示例 1：
```
输入: [1,6,3,2,5]
输出: false
```
示例 2：
```
输入: [1,3,2,6,5]
输出: true
```

提示：

- `数组长度 <= 1000`

## Solution

### Recursion

后序遍历的模式是：

```
[ 左子树 , 右子树 , 根节点 ]
```

因此，最后一个节点一定是根节点。由于题目中已知树应为二叉搜索树，可以利用二叉搜索树的特性来判断右子树开始的位置：

- 左子树的元素都一定**小于**根节点。
- 右子树的元素都一定**大于**根节点。

因此，我们可以从头遍历数组，找到第一个大于根节点的值，其位置至根节点之间，即为右子树元素。

此时，我们得到了如下索引：

```
[ 左子树 , 右子树 , 根节点 ]
          ^         ^
       rightIdx  rootIdx
```

左子树为 `[0:rightIdx)`，由于我们一开始是寻找的第一个大于根节点的节点作为左右子树分界值，因此不用再校验左子树与根的关系。

右子树为 `[rightIdx:rootIdx)`，遍历这部分元素，校验里面的值是否都大于根节点。若有非法值，则说明该数组不是二叉搜索树的后序遍历结果。

若到目前为止，结果都符合预期，则要继续递归判断其左右子树的后序遍历序列，是否也都满足上述条件。

此方法的时间复杂度为 O(n^2)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2 MB


```go
func verifyPostorder(postorder []int) bool {
    if len(postorder) == 0 {
        return true
    }

    rootIdx := len(postorder) - 1
    rightIdx := 0
    for ; rightIdx < rootIdx; rightIdx++ {
        if postorder[rightIdx] > postorder[rootIdx] {
            break
        }
    }
    // left sub-tree: [0:rightIdx)
    // right sub-tree: [rightIdx:rootIdx)
    for i := rightIdx; i < rootIdx; i++ {
        if postorder[i] < postorder[rootIdx] {
            // invalid right sub-tree node
            return false
        }
    }

    return verifyPostorder(postorder[:rightIdx]) && // left sub-tree
            verifyPostorder(postorder[rightIdx:rootIdx]) // right sub-tree
}
```

### Monotonic Stack

TODO 单调栈方法 https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/ 
