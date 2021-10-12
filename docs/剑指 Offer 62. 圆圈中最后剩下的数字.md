<!-- omit in toc -->
# 剑指 Offer 62.  圆圈中最后剩下的数字

- Difficulty: Easy
- Topics: `Recursion`, `Math`
- Link: https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Simulation](#simulation)
    - [Go (Time Limit Exceeded)](#go-time-limit-exceeded)
  - [Math](#math)
    - [Go](#go)

## Description

0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


示例 1：
```
输入: n = 5, m = 3
输出: 3
```
示例 2：
```
输入: n = 10, m = 17
输出: 2
```

限制：

- `1 <= n <= 10^5`
- `1 <= m <= 10^6`

## Solution

### Simulation

模拟的方法，以线性链表模拟「圆圈」，每移动 `m` 次就删除一个节点，直到长度为 `1` 为止。

模拟方法的时间复杂度为 O(n*m)，空间复杂度为 O(n)。

#### Go (Time Limit Exceeded)

```go
func lastRemaining(n int, m int) int {
    circle := list.New()
    for i := 0; i < n; i++ {
        circle.PushBack(i)
    }

    e := circle.Front()
    for circle.Len() > 1 {
        for i := 0; i < m-1; i++ {
            if e == nil {
                e = circle.Front().Next()
            } else if e.Next() == nil {
                // tail
                e = circle.Front()
            } else {
                e = e.Next()
            }
        }
        next := e.Next()
        circle.Remove(e)
        e = next
    }

    return circle.Front().Value.(int)
}
```

### Math

这题描述的其实就是[约瑟夫环问题](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98)，较为详细的数学推导可见这篇[知乎文章](https://zhuanlan.zhihu.com/p/121159246)，基本与《剑指 Offer》书中推导相符，不过更加详细，包括 `% n` 是由分队推导得来也有一定阐述。

设 $f(n, m)$ 为 n 个数字，每 m 个删除一次后最后得到的结果。最后的递推式为：

$$
f(n, m) = \begin{cases}
0, & n = 1 \\ 
(f(n-1, m) + m) \% n, & n > 1 \\
\end{cases}
$$

其中：
- $f(n, m)$ 为共有 n 个数字，每 m 个数字删除一次，最后剩余的数字值。
- $f(n-1, m)$ 为共有 n-1 个数字（或为 n 个数字删除了第 m 个数字之后的列表），每 m 个数字删除一次，最后剩余的数字值。

该方法的时间复杂度为 O(n)，迭代的空间复杂度为 O(1)，递归的空间复杂度为 O(n)。

#### Go

迭代方法。

- 执行用时: 4 ms
- 内存消耗: 1.9 MB

```go
func lastRemaining(n int, m int) int {
    ans := 0 
    for i := 2; i <= n; i++ {
        ans = (ans + m) % i
    }

    return ans
}
```

递归方法。

- 执行用时: 12 ms
- 内存消耗: 9.6 MB

```go
func lastRemaining(n int, m int) int {
    if n == 1 {
        return 0
    }

    return ( lastRemaining(n-1, m) + m ) % n
}
```
