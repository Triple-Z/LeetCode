<!-- omit in toc -->
# 剑指 Offer 30.  用两个栈实现队列

- Difficulty: Easy
- Topics: `Stack`, `Design`, `Queue`
- Link: https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

- [Description](#description)
- [Solution](#solution)
  - [In and Out Stacks](#in-and-out-stacks)
    - [Go](#go)

## Description

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 `appendTail` 和 `deleteHead` ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，`deleteHead` 操作返回 -1 )

 

示例 1：

```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

示例 2：

```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

提示：

- `1 <= values <= 10000`
- `最多会对 appendTail、deleteHead 进行 10000 次调用`


## Solution

### In and Out Stacks

新建两个栈，两个 Stack 分别作为 in stack 和 out stack ，in stack 倒入 out stack ；out stack 不需要倒回 in stack ，直接取 out stack 的栈顶元素即可。

#### Go

Go 中的动态数据结构在 `container` 包中，此题可以使用 `list.List` 。

- 执行用时: 176 ms
- 内存消耗: 8.4 MB

```go
type CQueue struct {
    s1 []int
    s2 []int
}


func Constructor() CQueue {
    return CQueue{
        s1: []int{},
        s2: []int{},
    }
}


func (this *CQueue) AppendTail(value int)  {
    // add value to stack 1
    this.s1 = append(this.s1, value)
}


func (this *CQueue) DeleteHead() int {
    
    if len(this.s2) == 0 {
        // move all elements from stack 1 to stack 2
        for len(this.s1) > 0 {
            m := this.s1[len(this.s1) - 1]
            this.s2 = append(this.s2, m)
            this.s1 = this.s1[:len(this.s1) - 1]
        }
        // clear stack 1
        this.s1 = []int{}
    }
    

    if len(this.s2) > 0 {
        // remove the top element
        head := this.s2[len(this.s2) - 1]
        this.s2 = this.s2[:len(this.s2) - 1]
        return head
    }

    return -1
}
```
