<!-- omit in toc -->
# 剑指 Offer 14 - II.  剪绳子 II

- Difficulty: Medium
- Topics: `Math`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/

- [Description](#description)
- [Solution](#solution)

## Description

给你一根长度为 `n` 的绳子，请把绳子剪成整数长度的 `m` 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 `k[0],k[1]...k[m - 1]` 。请问 `k[0]*k[1]*...*k[m - 1]` 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```
示例 2:
```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```

提示：

- `2 <= n <= 1000`

注意：本题与 [343 题](./343.%20Integer%20Break%20整数拆分.md) 相同。


## Solution

由于数值可能过大，该题需要使用模除。根据 [剑指 Offer 14 - I. 剪绳子](./剑指%20Offer%2014%20-%20I.%20剪绳子.md) ，我们已知应该尽可能获得长度为 3 的绳子。因此可以直接使用贪婪的方法求得结果。

具体解法可见 [343 题的贪婪方法](./343.%20Integer%20Break%20整数拆分.md#math-greedy)。
