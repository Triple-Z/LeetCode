<!-- omit in toc -->
# 剑指 Offer 42.  连续子数组的最大和

- Difficulty: Easy
- Topics: `Array`, `Divide and Conquer`, `Dynamic Programming`
- Link: https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Dynamic Programming](#dynamic-programming)
    - [Go](#go)
  - [Divide and Conquer](#divide-and-conquer)
    - [Lang](#lang)

## Description

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
 

示例1:
```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

提示：

- `1 <= arr.length <= 10^5`
- `-100 <= arr[i] <= 100`

## Solution

### Dynamic Programming

由于要找出连续子数组的最大和，那自然就想到了前缀和的方法。通过一个 `dp` 数组来存储当前元素可获得的最大子数组和，递推方程如下：

$$
dp(i) = \begin{cases}
    nums[0], & i = 0 \\
    max(nums[i], nums[i] + dp(i-1))， & i > 0
\end{cases}
$$

#### Go

- 执行用时: 20 ms
- 内存消耗: 8.1 MB

```go
func maxSubArray(nums []int) int {
    dp := make([]int, len(nums))
    ans := nums[0]

    dp[0] = nums[0]
    for i := 1; i < len(nums); i++ {
        dp[i] = max(nums[i], nums[i] + dp[i-1])
        ans = max(ans, dp[i])
    }

    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### Divide and Conquer

TODO: 分治法 https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/lian-xu-zi-shu-zu-de-zui-da-he-by-leetco-tiui/

#### Lang

```lang
2nd solution code goes here.
```