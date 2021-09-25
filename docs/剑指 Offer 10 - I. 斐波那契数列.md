<!-- omit in toc -->
# 剑指 Offer 10 - I.  斐波那契数列

- Difficulty: Easy
- Topics: `Memoization`, `Math`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)
  - [Quick Pow](#quick-pow)
    - [Lang](#lang)

## Description

写一个函数，输入 `n` ，求斐波那契（Fibonacci）数列的第 `n` 项（即 `F(N)`）。斐波那契数列的定义如下：
```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
```
输入：n = 2
输出：1
```
示例 2：
```
输入：n = 5
输出：5
```

提示：
- `0 <= n <= 100`

## Solution

### Dynamic Programming

典型的动态规划，利用已计算的子问题结果来得出当前问题结果。

斐波那契的递推式在题目中已经给出，如下：
$$
F(N) = \begin{cases}
   0, & N = 0 \\
   1, & N = 1 \\
   F(N-1) + F(N-2), & N>1
\end{cases}
$$

#### Go

- 执行用时: 0 ms
- 内存消耗: 2 MB

```go
func fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    }

    dp := make([]int, n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i := 2; i <= n; i++ {
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    }

    return dp[n]
}
```

### Quick Pow

TODO: 矩阵快速幂，https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/

#### Lang

```lang
2nd solution code goes here.
```