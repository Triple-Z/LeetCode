<!-- omit in toc -->
# 剑指 Offer 46.  把数字翻译成字符串

- Difficulty: Medium
- Topics: `String`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)
  - [Backtrack](#backtrack)
    - [Lang](#lang)

## Description

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:
```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

提示：
```
0 <= num < 231
```

## Solution

### Dynamic Programming

先将数字各位拆成数组，再做进一步处理，如 `12258` 变为 `[1, 2, 2, 5, 8]` 。

由于数字翻译成字母的规则是 `0->a, 1->b, ... 25->z` ，因此在某位结束，能获取到的翻译方法应该是以下两者之和：
1. 若该位能转换为一个 `0-9` 对应的字母（必然成立），则能够得到上一位数字能获取到的翻译方法数量。
2. 若该位与上一位要能组成 `10-25` 之间的数字，则能够得到上上位数字能获取到的翻译方法数量。

因此递归方程如下：

$$
dp(i) = \begin{cases}
1, & i = 0 \text{ or } (i = 1 \text{ and } n(0, 1) >= 26 ) \\
2, & i = 1 \text{ and } n(0, 1) < 26 \\
dp(i-1), & 0 \le n(i-1, i) < 10 \text{ or } n(i-1, i) > 25 \\
dp(i-1) + dp(i-2), & 10 \le n(i-1, i) < 26
\end{cases}
\newline
s.t. \text{  } n(a, b) = digits[a] * 10 + digits[b]
$$

此方法时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func translateNum(num int) int {
    if num < 10 {
        return 1
    } else if num < 26 {
        return 2
    }

    // get the digits
    tmp := num
    digits := []int{}
    for tmp != 0 {
        digit := tmp % 10
        tmp /= 10
        digits = append(digits, digit)
    }

    // reverse digits
    for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
        digits[i], digits[j] = digits[j], digits[i]
    }

    dp := make([]int, len(digits))
    dp[0] = 1
    if digits[0] * 10 + digits[1] < 26 {
        dp[1] = 2
    } else {
        dp[1] = 1
    }

    for i := 2; i < len(digits); i++ {
        n := digits[i-1] * 10 + digits[i]
        dpIMinusTwo := 0
        if 10 <= n && n < 26 {
            dpIMinusTwo = dp[i-2]
        }

        dp[i] = dp[i-1] + dpIMinusTwo
    }

    return dp[len(digits)-1]
}
```

Go 中整数转换为字符串：`strconv.Itoa(i int) string` 。

### Backtrack

TODO

#### Lang

```lang
2nd solution code goes here.
```