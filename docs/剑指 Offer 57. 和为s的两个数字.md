<!-- omit in toc -->
# 剑指 Offer 57.  和为s的两个数字

- Difficulty: Easy
- Topics: `Array`, `Two Pointers`, `Binary Search`
- Link: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Hash Table](#hash-table)
    - [Go](#go)
  - [Two Pointers](#two-pointers)
    - [Go](#go-1)

## Description

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：
```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
```
示例 2：
```
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
```

限制：

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`


## Solution

### Hash Table

由于要找出数组中某两个数之和等于目标值，我们可以将遍历过的值记录在哈希表中，当往下遍历时，只需查找哈希表内容，是否存在 `target - num` 的数值，若存在则说明数组中存在符合要求的数字对，输出即可。

#### Go

- 执行用时: 200 ms
- 内存消耗: 9.8 MB

```go
func twoSum(nums []int, target int) []int {
    numMap := make(map[int]bool)
    for i := 0; i < len(nums); i++ {
        if _, ok := numMap[target - nums[i]]; ok {
            return []int{nums[i], target-nums[i]}
        }
        numMap[nums[i]] = true
    }

    return nil
}
```

### Two Pointers

左右双指针。将左指针放置于最左边，右指针放置于最右边。退出条件为两指针相遇，指针移动的规则如下：
- 若两指针的值之和大于目标值，则移动右指针 `right--` 。
- 若两指针的值之和小于目标值，则移动左指针 `left++`。
- 若两指针的值之和等于目标值，则将当前两指针的值返回。

此方法时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 164 ms
- 内存消耗: 8.9 MB

```go
func twoSum(nums []int, target int) []int {
    p, q := 0, len(nums)-1
    for p < q {
        sum := nums[p] + nums[q]
        if sum > target {
            q--
        } else if nums[p] + nums[q] == target {
            return []int{nums[p], nums[q]}
        } else {
            p++
        }
    }

    return []int{}
}
```