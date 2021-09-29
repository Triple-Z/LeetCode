<!-- omit in toc -->
# 剑指 Offer 25.  合并两个排序的链表

- Difficulty: Easy
- Topics: `Recursion`, `Linked List`
- Link: https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Two Pointers](#two-pointers)
    - [Go](#go)

## Description

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```
限制：
```
0 <= 链表长度 <= 1000
```

## Solution

### Two Pointers

合并两个有序链表，典型的双指针问题。该题最简单的做法是不操作原有链表，利用 O(m+n) 的空间复杂度，返回一个新创建的链表。当然，我们肯定要思考如何做就地转换，用 O(1) 的空间复杂度来实现。

其实就地处理的方法也不复杂，只需要借助三个指针（`cur` 、`p` 、`q` ）。其中，`cur` 是指向新链表当前节点的指针，`p` 和 `q` 则分别是指向 `l1` 、`l2` 当前节点的指针。为了降低代码的复杂度，我们可以创建一个 dummy head ，很方便地处理“谁作为 head”这个特殊问题。

然后就是循环判断部分，若我们选中了两链表中的一个值，要将其链接到新的有序链表中，只需要作如下的操作：
```go
// selected can be "p" or "q"
cur.Next = selected
selected = selected.Next
cur = cur.Next
```

最后若有一个链表已经处理完成，还剩下另一个链表的一些节点，则直接将结果有序链表与链表剩下的内容拼接起来即可。

```go
// remains can be "p" or "q"
if remains != nil {
	cur.Next = remains
}
```

该方法的时间复杂度为 O(m+n)，由于只创建了一个 dummy head，空间复杂度为 O(1)。

#### Go

- 执行用时: 4 ms
- 内存消耗: 4.1 MB

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    p, q := l1, l2
    var dummyHead *ListNode = &ListNode{}
    cur := dummyHead

    for p != nil && q != nil {
        if p.Val <= q.Val {
            // use p
            cur.Next = p
            p = p.Next
        } else {
            // use q
            cur.Next = q
            q = q.Next
        }
        cur = cur.Next
    }

    if p != nil {
        cur.Next = p
    }

    if q != nil {
        cur.Next = q
    }

    return dummyHead.Next
}
```
