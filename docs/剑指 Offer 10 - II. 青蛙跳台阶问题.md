<!-- omit in toc -->
# 剑指 Offer 10 - II.  青蛙跳台阶问题

- Difficulty: Easy
- Topics: `Memoization`, `Math`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)

## Description

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
```
输入：n = 2
输出：2
```
示例 2：
```
输入：n = 7
输出：21
```
示例 3：
```
输入：n = 0
输出：1
```
提示：

- `0 <= n <= 100`

## Solution

### Dynamic Programming

典型的动态规划问题，由于青蛙可以一次跳一格，也可以一次跳两格，那么很容易得到递推方程：

$$
dp(i) = dp(i-1) + dp(i-2),\space \text{s.t.} \space dp(0) = dp(1) = 1
$$

#### Go

- 执行用时: 0 ms
- 内存消耗: 2 MB

```go
func numWays(n int) int {
    if n == 0 {
        return 1
    } else if n == 1 {
        return 1
    }

    dp := make([]int, n+1)
    dp[0] = 1
    dp[1] = 1

    for i := 2; i <= n; i++ {
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    }

    return dp[n]
}
```
