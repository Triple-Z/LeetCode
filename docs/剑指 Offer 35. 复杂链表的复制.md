<!-- omit in toc -->
# 剑指 Offer 35.  复杂链表的复制

- Difficulty: Medium
- Topics: `Hash Table`, `Linked List`
- Link: https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

- [Description](#description)
- [Solution](#solution)

## Description

请实现 `copyRandomList` 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 `next` 指针指向下一个节点，还有一个 `random` 指针指向链表中的任意节点或者 `null`。


示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png)
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```
示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)
```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```
示例 3：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)
```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```
示例 4：
```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```

提示：

- `-10000 <= Node.val <= 10000`
- `Node.random` 为空（null）或指向链表中的节点。
- 节点数目不超过 1000 。

注意：本题与 [138 题](./138.%20Copy%20List%20with%20Random%20Pointer%20复制带随机指针的链表.md) 相同。

## Solution

见 [138 题题解](./138.%20Copy%20List%20with%20Random%20Pointer%20复制带随机指针的链表.md#Solution)。

