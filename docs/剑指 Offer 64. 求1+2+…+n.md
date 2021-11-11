<!-- omit in toc -->
# 剑指 Offer 64.  求1+2+…+n

- Difficulty: Medium
- Topics: `Bit Manipulation`, `Recursion`, `Brainteaser`
- Link: https://leetcode-cn.com/problems/qiu-12n-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Recursion](#recursion)
    - [Go](#go)

## Description

求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


示例 1：
```
输入: n = 3
输出: 6
```
示例 2：
```
输入: n = 9
输出: 45
```
限制：

- `1 <= n <= 10000`

## Solution

### Recursion

递归进行求和计算，但是用逻辑与的短路特性来代替 `if` 条件语句。

时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.7 MB

```go
func sumNums(n int) int {
    ans := 0
    var sum func(int) bool
    sum = func(n int) bool {
        ans += n
        return n > 0 && sum(n-1)
    }
    sum(n)
    return ans
}
```