<!-- omit in toc -->
# 剑指 Offer 63.  股票的最大利润

- Difficulty: Medium
- Topics: `Array`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/

- [Description](#description)
- [Solution](#solution)
  - [One-Time Tranversal](#one-time-tranversal)
    - [Go](#go)

## Description

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```
示例 2:
```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

限制：
```
0 <= 数组长度 <= 10^5
```

## Solution

### One-Time Tranversal

由于只能买卖股票一次，因此可以在遍历的过程中，记录过去时间的股票价格最小值，就可得到如果当日卖出所能获得到的最大利润。因此只要找出”每日卖出获得到的最大利润“的最大值，即可得到答案。

此方法的时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 4 ms
- 内存消耗: 3 MB

```go
func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }

    minPrice := prices[0]
    ans := math.MinInt64
    for i := 0; i < len(prices); i++ {
        minPrice = min(minPrice, prices[i])
        ans = max(ans, prices[i] - minPrice)
    }

    return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
