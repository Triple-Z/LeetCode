<!-- omit in toc -->
# 剑指 Offer 11.  旋转数组的最小数字

- Difficulty: Easy
- Topics: `Array`, `Binary Search`
- Link: https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Reversal Iteration](#reversal-iteration)
    - [Go](#go)
  - [Binary Search](#binary-search)

## Description

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 `[3,4,5,1,2]` 为 `[1,2,3,4,5]` 的一个旋转，该数组的最小值为1。  

示例 1：
```
输入：[3,4,5,1,2]
输出：1
```
示例 2：
```
输入：[2,2,2,0,1]
输出：0
```

## Solution

### Reversal Iteration

从后往前遍历，有序递增数组由于被旋转，后往前应先递减，直到一次递增后再递减。因此只要找到了这个递增的“门槛”，就能确定出旋转后数组最小的值。

当遍历值比之前记录的最小值要大，那么就找到了“门槛”，返回记录的最小值即可。

#### Go

- 执行用时: 4 ms
- 内存消耗: 3.1 MB

```go
func minArray(numbers []int) int {
    min := math.MaxInt64
    for i := len(numbers)-1; i >= 0; i-- {
        if numbers[i] > min {
            return min
        }
        min = Min(min, numbers[i])
    }
    return min
}

func Min(a int, b int) int {
    if a < b {
        return a
    }
    
    return b
}
```

### Binary Search

TODO: I don't know how.
