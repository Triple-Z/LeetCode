<!-- omit in toc -->
# 剑指 Offer 53 - I.  在排序数组中查找数字 I

- Difficulty: Easy
- Topics: `Array`, `Binary Search`
- Link: https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)
  - [Binary Search](#binary-search)

## Description

统计一个数字在排序数组中出现的次数。

 

示例 1:
```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```
示例 2:
```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

提示：

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `nums 是一个非递减数组`
- `-109 <= target <= 109`

注意：本题与 [34 题](./34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array%20在排序数组中查找元素的第一个和最后一个位置.md) 相同（仅返回值不同）。

## Solution

### Iteration

直接遍历查找 target。

#### Go

- 执行用时: 4 ms
- 内存消耗: 3.9 MB

```go
func search(nums []int, target int) int {
    // brute-force
    sum := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] == target {
            sum++
        } else if nums[i] > target {
            break
        }
    }
    return sum
}
```

### Binary Search

可以用二分来找到目标值，一轮二分找到起点，一轮二分找到终点。
Binary Search 时间复杂度为 O(logn) 。

TODO
