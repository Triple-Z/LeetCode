<!-- omit in toc -->
# 剑指 Offer 06.  从尾到头打印链表

- Difficulty: Easy
- Topics: `Stack`, `Recursion`, `Linked List`, `Two Pointers`
- Link: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Stack](#stack)
    - [Go](#go)

## Description


输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


示例 1：
```
输入：head = [1,3,2]
输出：[2,3,1]
```

限制：
```
0 <= 链表长度 <= 10000
```

## Solution

### Stack

创建一个栈，按线性序遍历链表，同时将遍历的元素逐个压入栈中。接着将栈中的元素逐个取出，并将其存入数组中。


#### Go

- 执行用时: 0 ms
- 内存消耗: 3.6 MB

```go
func reversePrint(head *ListNode) []int {
    s := list.New()

    p := head
    for p != nil {
        s.PushBack(p.Val)
        p = p.Next
    }da

    ans := []int{}
    for s.Len() != 0 {
        ans = append(ans, s.Remove(s.Back()).(int))
    }

    return ans
}
```
