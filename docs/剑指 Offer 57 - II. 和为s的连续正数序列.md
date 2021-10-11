<!-- omit in toc -->
# 剑指 Offer 57 - II.  和为s的连续正数序列

- Difficulty: Easy
- Topics: `Math`, `Two Pointers`, `Enumeration`
- Link: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Brute-force](#brute-force)
    - [Go](#go)
  - [Two Pointers](#two-pointers)
    - [Go](#go-1)

## Description

输入一个正整数 `target` ，输出所有和为 `target` 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
```
输入：target = 9
输出：[[2,3,4],[4,5]]
```
示例 2：
```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

限制：

- `1 <= target <= 10^5`

## Solution

### Brute-force

最简单的方法当然就是两层循环遍历啦，不过可以稍微做的聪明点。由于是要求和为 `target` 的**连续**正整数序列，可以很显然得到以下两个条件：
1. 起点一定位于 `target / 2` 及其之前，否则肯定超过目标值。
2. 重点一定位于 `target / 2 + 1` 及其之前，否则肯定超过目标值。

两层 `for` 循环遍历累加，达到目标值则将 `[i, ..., j]` 塞入结果中。

时间复杂度为 O(n^2)，空间复杂度为 O(1)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.2 MB

```go
func findContinuousSequence(target int) [][]int {
    ans := [][]int{}
    for i := 1; i <= target / 2; i++ {
        sum := i
        for j := i + 1; j <= target / 2 + 1; j++ {
            sum += j
            if sum == target {
                // from i to j is valid
                l := []int{}
                for k := i; k <= j; k++ {
                    l = append(l, k)
                }
                ans = append(ans, l)
                break
            } else if sum > target {
                break
            }
        }
    }

    return ans
}
```

### Two Pointers

使用左右两个指针作为「窗口」，起始时两指针分别为 `1` 和 `2` ，退出条件为两指针相遇。且指针的移动条件如下：
1. 若窗口内的值之和**等于**目标值，则将该连续正数序列放入结果列表中，并移动左指针，使其之和变小。
2. 若窗口内的值之和**大于**目标值，则说明该序列值过大，移动左指针缩小窗口，使其之和变小。
3. 若窗口内的值之和**小于**目标值，则说明该序列值过小，移动右指针扩大窗口，使其之和变大。

那如何求得「窗口」中连续正数序列之和呢？答案很简单，通过小学数学中的等差数列求和式即可。

该方法时间复杂度为 O(n)，空间复杂度为O(1)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.2 MB

```go
func findContinuousSequence(target int) [][]int {
    i, j := 1, 2
    ans := [][]int{}
    for i < j {
        sum := (j - i + 1) * (i + j) / 2
        if sum == target {
            li := []int{}
            for k := i; k <= j; k++ {
                li = append(li, k)
            }
            ans = append(ans, li)
            i++
        } else if sum > target {
            i++
        } else {
            j++
        }
    }

    return ans
}
```