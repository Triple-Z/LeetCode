<!-- omit in toc -->
# 剑指 Offer 28.  对称的二叉树

- Difficulty: Easy
- Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`
- Link: https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

- [Description](#description)
- [Solution](#solution)

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

注意：本题与 [101 题](./101.%20Symmetric%20Tree%20对称二叉树.md) 相同。

## Solution

见 [101 题题解](./101.%20Symmetric%20Tree%20对称二叉树.md#Solution)。