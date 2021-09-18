<!-- omit in toc -->
# 剑指 Offer 30.  包含min函数的栈

- Difficulty: Easy
- Topics: `Stack`, `Design`
- Link: https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Two Stacks](#two-stacks)
    - [Go](#go)

## Description

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 `O(1)`。


示例:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```

提示：
- 各函数的调用总次数不超过 20000 次


## Solution

### Two Stacks

使用一个栈和一个存有当前最小数的辅助栈即可完成。

push：将数值压入栈中，同时确认若当前值比上一个最小值要小，则将当前值同时压入辅助栈，否则再将上一个最小值作为当前最小值，压入辅助栈。

pop：同时将栈和辅助栈的栈顶元素推出。

min：返回辅助栈栈顶元素即为当前栈中元素最小值。

#### Go

- 执行用时: 16 ms
- 内存消耗: 8 MB

```go
type MinStack struct {
    minStack []int
    s []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{
        minStack: []int{},
        s: []int{},
    }
}


func (this *MinStack) Push(x int)  {
    this.s = append(this.s, x)

    if len(this.minStack) == 0 || x < this.minStack[len(this.minStack) - 1] {
        this.minStack = append(this.minStack, x)
        return
    }

    this.minStack = append(this.minStack, this.minStack[len(this.minStack) - 1])
}


func (this *MinStack) Pop() {
    this.s = this.s[:len(this.s) - 1]
    this.minStack = this.minStack[:len(this.minStack) - 1]
}


func (this *MinStack) Top() int {
    return this.s[len(this.s) - 1]
}

func (this *MinStack) Min() int {
    return this.minStack[len(this.minStack) - 1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
