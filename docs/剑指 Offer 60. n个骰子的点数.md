<!-- omit in toc -->
# 剑指 Offer 60.  n个骰子的点数

- Difficulty: Medium
- Topics: `Math`, `Dynamic Programming`, `Probability and Statistics`
- Link: https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)

## Description

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
```
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
```
示例 2:
```
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```

限制：

- `1 <= n <= 11`


## Solution

### Dynamic Programming

TODO：以为自己懂了，其实没懂。

https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/jian-zhi-offer-60-n-ge-tou-zi-de-dian-sh-z36d/

概率 DP：https://oi-wiki.org/dp/probability/

#### Go

> FIXME: 翻译的剑指 Offer 中给出的答案。

- 执行用时: 0 ms
- 内存消耗: 2 MB

```go
// translate from Sword to Offer
func dicesProbability(n int) []float64 {
    if n < 1 {
        return []float64{}
    }

    dp := make([][]int, 2)
    for i := 0; i < 2; i++ {
        dp[i] = make([]int, 6 * n + 1)
    }

    flag := 0

    for i := 1; i <= 6; i++ {
        dp[flag][i] = 1
    }

    for k := 2; k <= n; k++ {
        for i := 0; i < k; i++ {
            // there are k dices, so the min sum will be k.
            dp[1 - flag][i] = 0
        }

        for i := k; i <= 6 * k; i++ {
            // calc from k to 6*k
            dp[1 - flag][i] = 0
            for j := 1; j <= 6 && j < i; j++ {
                dp[1 - flag][i] += dp[flag][i - j]
            }
        }
        // switch dice results
        flag = 1 - flag
    }

    total := math.Pow(6, float64(n))
    ans := []float64{}
    for i := n; i <= n * 6; i++ {
        ans = append(ans, float64(dp[flag][i]) / total)
    }
    
    return ans
}
```
