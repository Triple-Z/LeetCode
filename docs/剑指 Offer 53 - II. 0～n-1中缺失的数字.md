<!-- omit in toc -->
# 剑指 Offer 53 - II.  0～n-1中缺失的数字

- Difficulty: Easy
- Topics: `Bit Manipulation`, `Array`, `Hash Table`, `Math`, `Binary Search`
- Link: https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)

## Description

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
```
输入: [0,1,3]
输出: 2
```
示例 2:
```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```

限制：
```
1 <= 数组长度 <= 10000
```

## Solution

### Iteration

数组中的每个数字都应该等于它的下标，遍历找出不等于的那个元素，返回当前的下标即为缺失的数字。

若没有找到缺失的数字，则认为缺失值位于最后，则返回当前数组大小即可。

#### Go

- 执行用时: 16 ms
- 内存消耗: 6.1 MB

```go
func missingNumber(nums []int) int {
    for i := 0; i < len(nums); i++ {
        if nums[i] != i {
            return i
        }
    }

    return len(nums)
}
```
