<!-- omit in toc -->
# 剑指 Offer 59 - II.  队列的最大值

- Difficulty: Medium
- Topics: `Design`, `Queue`, `Monotonic Queue`
- Link: https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Monotonic Queue](#monotonic-queue)
    - [Go](#go)

## Description

请定义一个队列并实现函数 `max_value` 得到队列里的最大值，要求函数`max_value`、`push_back` 和 `pop_front` 的均摊时间复杂度都是O(1)。

若队列为空，`pop_front` 和 `max_value` 需要返回 -1

示例 1：
```
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
```
示例 2：
```
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
```

限制：

- `1 <= push_back,pop_front,max_value的总操作数 <= 10000`
- `1 <= value <= 10^5`

## Solution

### Monotonic Queue

此题作为 [剑指 Offer 59 - I. 滑动窗口的最大值](./剑指%20Offer%2059%20-%20I.%20滑动窗口的最大值.md) 的延伸，自然是使用类似的方法。

为了实现一个能随时获取最大值的队列，我们自然要像 [剑指 Offer 30. 包含min函数的栈](./剑指%20Offer%2030.%20包含min函数的栈.md) 一样，采用一个双端队列作为辅助队列来记录当前队列中的最大值。那么怎么利用这个辅助队列，就是是否能够在 O(1) 下获取到队列最大值的关键了。

首先要明确地是，这个辅助数组是用于存储当前队列中的最大值。如果这个辅助数组是一个单调递减的队列，那么当前的队列最大值将永远位于队首。那如何让辅助队列成为一个单调递减的队列呢？其实很简单，只要遵循如下规则即可。

- Push：在插入元素时，将队列中所有小于当前元素的值全部从队尾弹出，再将当前元素插入队尾。保持队列的单调递减。
- Pop：在弹出元素时，需要检查队首是否为弹出的元素。如果是，需要同时也将队首元素弹出。

只需要遵循如上规则，就能轻松维护一个单调递减的辅助队列，从而实现队列的最大值的 O(1) 获取。

该方法下，`max_value`、`push_back` 和 `pop_front` 的均摊时间复杂度都是 O(1)，空间复杂度为 O(n)。

#### Go

```go
type MaxQueue struct {
    queue []int
    maxQueue []int
}


func Constructor() MaxQueue {
    return MaxQueue{
        queue: []int{},
        maxQueue: []int{},
    }
}


func (this *MaxQueue) Max_value() int {
    if len(this.maxQueue) < 1 {
        return -1
    }

    return this.maxQueue[0]
}


func (this *MaxQueue) Push_back(value int)  {
    this.queue = append(this.queue, value)

    // remove less than value from queue tail
    for len(this.maxQueue) > 0 && this.maxQueue[len(this.maxQueue)-1] < value {
        this.maxQueue = this.maxQueue[:len(this.maxQueue)-1]
    }
    this.maxQueue = append(this.maxQueue, value)
}


func (this *MaxQueue) Pop_front() int {
    if len(this.queue) < 1 {
        return -1
    }

    value := this.queue[0]
    this.queue = this.queue[1:]
    if len(this.maxQueue) > 0 && value == this.maxQueue[0] {
        this.maxQueue = this.maxQueue[1:]
    }

    return value
}


/**
 * Your MaxQueue object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Max_value();
 * obj.Push_back(value);
 * param_3 := obj.Pop_front();
 */
```
