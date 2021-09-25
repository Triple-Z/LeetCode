<!-- omit in toc -->
# 剑指 Offer 35.  复杂链表的复制

- Difficulty: Medium
- Topics: `Hash Table`, `Linked List`
- Link: https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Hash Table](#hash-table)
    - [Go](#go)
  - [No Extra Space](#no-extra-space)
    - [Lang](#lang)

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


## Solution

### Hash Table

复制链表并不难，只要先创建一个 Dummy Head，然后遍历原链表，每次都将原链表的节点复制一份，并将复制的节点指向原节点的下一个节点，最后将原链表的节点指向复制的节点。

该题中的难点在于 Random 指针的复制。我们需要一个机制，能够将原链表的节点和新链表对应起来，那自然而然就是哈希表了。

我们可以新建一个节点映射表，key 是原链表中节点的地址，value 是新链表中对应复制节点的地址。当复制好链表后，我们可以遍历一次复制好的链表，将 Random 指针内容修改为新链表中对应的节点即可。

此方法的时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 3.5 MB

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }

    var cur *Node = head
    var newHead Node = Node{}
    var newCur *Node = &newHead  // dummy head

    nodeMap := make(map[*Node]*Node) // key: old node, value: new node

    // copy list
    for cur != nil {
        newNode := Node{
            Val: cur.Val,
            Random: cur.Random,
        }
        newCur.Next = &newNode
        nodeMap[cur] = &newNode
        cur = cur.Next
        newCur = newCur.Next  // to newNode
    }

    // reset random pointer for copied list
    newCur = newHead.Next
    for newCur != nil {
        newCur.Random = nodeMap[newCur.Random]
        newCur = newCur.Next
    }

    return newHead.Next
}
```

### No Extra Space

TODO: 将新节点先接在老节点后面，再将新节点的 Random 赋值为目标老节点的后一个节点（即为目标的新节点），最后再将新老链表拆离，返回新链表。

#### Lang

```lang
2nd solution code goes here.
```
