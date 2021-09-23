<!-- omit in toc -->
# 剑指 Offer 03.  数组中重复的数字

- Difficulty: Easy
- Topics: `Array`, `Hash Table`, `Sorting`
- Link: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Hash Table](#hash-table)
    - [Go](#go)

## Description

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

限制：
```
2 <= n <= 100000
```

## Solution

### Hash Table

遍历一遍，将内容塞入哈希表。若遍历到的内容已经在哈希表存在，则立即返回。

#### Go

- 执行用时: 36 ms
- 内存消耗: 9.7 MB

```go
func findRepeatNumber(nums []int) int {
    nMap := make(map[int]int)
    for _, n := range nums {
        if _, ok := nMap[n]; ok {
            return n
        }
        nMap[n] = 1
    }

    return -1
}
```
