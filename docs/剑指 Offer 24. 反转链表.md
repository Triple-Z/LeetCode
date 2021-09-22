<!-- omit in toc -->
# 剑指 Offer 24.  反转链表

- Difficulty: Easy
- Topics: `Recursion`, `Linked List`
- Link: https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)

## Description


定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


示例:
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

限制：
```
0 <= 节点个数 <= 5000
```
## Solution

### Iteration

标准反转链表，使用三个指针 `prev`， `cur` ，`next` ，核心代码就四行：

```go
next := cur.Next
cur.Next = prev
prev = cur
cur = next
```

只要遍历反转即可。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.5 MB

```go
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }

    cur := head.Next
    prev := head
    for cur != nil {
        next := cur.Next
        cur.Next = prev
        prev = cur
        cur = next
    }

    head.Next = nil
    return prev
}
```
