<!-- omit in toc -->
# 剑指 Offer 17.  打印从1到最大的n位数

- Difficulty: Easy
- Topics: `Array`, `Math`
- Link: https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)
  - [Big Number Problem](#big-number-problem)

## Description

输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```

说明：

- 用返回一个整数列表来代替打印
- n 为正整数

## Solution

### Iteration

根据 `n` 确定上限，遍历赋值即可。

时间复杂度为 O(10^n)，空间复杂度为 O(1) （生成的列表用于返回值）。

#### Go

执行用时: 8 ms
内存消耗: 7.1 MB

```go
func printNumbers(n int) []int {
    upper := pow(10, n)
    ans := make([]int, upper-1)

    for i := 0; i < len(ans); i++ {
        ans[i] = i + 1
    }

    return ans
}

func pow(base, n int) int {
    ans := 1
    for i := 0; i < n; i++ {
        ans *= base
    }
    return ans
}
```

### Big Number Problem

TODO：事实上这道题理应考的是大数问题，方法为回溯全排列。

https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
