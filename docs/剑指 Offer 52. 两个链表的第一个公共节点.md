<!-- omit in toc -->
# 剑指 Offer 52.  两个链表的第一个公共节点

- Difficulty: Easy
- Topics: `Hash Table`, `Linked List`, `Two Pointers`
- Link: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Two Pointers](#two-pointers)
    - [Go](#go)

## Description

输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

在节点 c1 开始相交。


示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png)
```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png)

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

示例 3：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
```

注意：

- 如果两个链表没有交点，返回 `null`.
- 在返回结果后，两个链表仍须保持原有的结构。
- 可假定整个链表结构中没有循环。
- 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

## Solution

### Two Pointers

由于两链表可能相交，题目要求我们要找出第一个相交点，很自然的就会想到双指针的方法。大体思路是根据两个链表的长度之差 k，让指向长链表的指针先走 k 步，这样两指针就能够一起移动，找出可能的相交节点。

> 此处的前提条件是，相交点不可能在长链表的 `[0, len-k-1]` 的节点上。链表相交之后部分的长度共享，因此相交点不可能在比较短链表更长的链表节点上。

对于链表，我们无法用类似数组的 `len()` 方法来快速得出链表的长度，只能遍历一次链表来获取，如：
```go
length := 0
for i := head; i != nil; i = i.Next {
	length++
}
```

因此我们一共将会对两个链表各遍历两次（第二次为一起遍历），该方法的时间复杂度为 O(m+n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 36 ms
- 内存消耗: 9.4 MB

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    // get A length
    lenA := 0
    for p := headA; p != nil; p = p.Next {
        lenA++
    }

    // get B length
    lenB := 0
    for q := headB; q != nil; q = q.Next {
        lenB++
    }

    diff := lenA - lenB
    p, q := headA, headB
    if diff < 0 {
        // B is longer than A
        diff = -diff
        for i := 0; i < diff; i++ {
            q = q.Next
        }
    } else {
        // A is longer than B
        for i := 0; i < diff; i++ {
            p = p.Next
        }
    }

    for p != nil && q != nil {
        if p == q {
            return p
        }
        p = p.Next
        q = q.Next
    }

    return nil

}
```
