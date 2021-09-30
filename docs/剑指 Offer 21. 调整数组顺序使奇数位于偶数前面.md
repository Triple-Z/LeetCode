<!-- omit in toc -->
# 剑指 Offer 21.  调整数组顺序使奇数位于偶数前面

- Difficulty: Easy
- Topics: `Array`, `Two Pointers`, `Sorting`
- Link: https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Two Pointers](#two-pointers)
    - [Go](#go)

## Description

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。


示例：
```
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
```

提示：

- `0 <= nums.length <= 50000`
- `1 <= nums[i] <= 10000`

## Solution

### Two Pointers

左右双指针遍历交换，由于奇数要在偶数前面，因此左指针负责寻找偶数，右指针负责寻找奇数。左右指针都分别找到偶数和奇数，则交换，否则进行右移或左移，直到找到偶数/奇数为止。当两指针相遇，代表交换结束，终止循环。

时间复杂度为 O(n)，算法为原地交换，空间复杂度为 O(1)。

#### Go

- 执行用时: 16 ms
- 内存消耗: 6.8 MB

```go
func exchange(nums []int) []int {
    p, q := 0, len(nums)-1
    for p < q {
        // odds in front, evens in end
        if nums[p] % 2 == 0 && nums[q] % 2 == 1 {
            nums[p], nums[q] = nums[q], nums[p]
        }
        if nums[p] % 2 != 0 {
            p++
        }
        if nums[q] % 2 != 1 {
            q--
        }
    }

    return nums
}
```
