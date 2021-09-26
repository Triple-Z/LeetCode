<!-- omit in toc -->
# 剑指 Offer 04.  二维数组中的查找

- Difficulty: Medium
- Topics: `Array`, `Binary Search`, `Divide and Conquer`, `Matrix`
- Link: https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Brute-force](#brute-force)
    - [Go](#go)
  - [Search from Top-Right](#search-from-top-right)
    - [Go](#go-1)

## Description

在一个 `n * m` 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


示例:

现有矩阵 matrix 如下：
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
给定 `target = 5`，返回 `true`。

给定 `target = 20`，返回 `false`。

限制：
- `0 <= n <= 1000`
- `0 <= m <= 1000`

## Solution

### Brute-force

暴力遍历一遍，依次判断元素的大小关系。

时间复杂度为 O(mn) ，空间复杂度为 O(1)。

#### Go

- 执行用时: 24 ms
- 内存消耗: 6.7 MB

```go
func findNumberIn2DArray(matrix [][]int, target int) bool {
    if len(matrix) == 0 {
        return false
    }

    // brute-force
    for i := 0; i < len(matrix); i++ {
        for j := 0; j < len(matrix[0]); j++ {
            if matrix[i][j] == target {
                return true
            }
        }
    }

    return false
}
```

### Search from Top-Right

由于该矩阵有行递增、列递增的性质，我们可以利用这一特点，进行找到一串元素中较为中间的值，通过对该值的判断，实现搜索空间的缩小。

在这样性质的矩阵中，有两个位置的元素满足这样的条件，那就是左下角（Bottom-Left）和右上角（Top-Right）元素。

之所以只能是左下角和右上角，而不能是左上角和右下角的原因是：左上角和右下角都是当前矩阵的极值（最小值和最大值），即使判断了目标值以及左上、右下值的关系，也没有办法能够继续缩小搜索空间。

![image-20210926220649197](assets/%E5%89%91%E6%8C%87%20Offer%2004.%20%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE/image-20210926220649197.png)

以右上角为例，对于当前矩阵范围，有以下三种情况，并对应不同的矩阵范围变化：
1. 右上角元素与目标元素相等：直接返回 `true` ，即矩阵中存在该目标元素。
2. 右上角元素大于目标元素：由于右上角元素为当前矩阵最右边一列最小元素，因此最右列的所有元素的值都大于目标元素，故将最右列排除（`j--`），缩小搜索空间，并对缩小后的矩阵继续比较新的右上角元素与目标元素的关系。
3. 右上角元素小于目标元素：由于右上角元素为当前矩阵最上边一列最大元素，因此最上行的所有元素的值都小于目标元素，故将最上行排除（`i++`），缩小搜索空间，并对缩小后的矩阵继续比较新的右上角元素与目标元素的关系。

只需至多 `n+m` 次操作，即可判断目标元素是否存在于矩阵中。

该方法的时间复杂度为 O(n+m)，空间复杂度为 O(1)。

#### Go

- 执行用时: 16 ms
- 内存消耗: 6.7 MB

```go
func findNumberIn2DArray(matrix [][]int, target int) bool {
    if len(matrix) == 0 {
        return false
    }

    n := len(matrix)
    m := len(matrix[0])

    // [i][j] is the top-right corner element
    i := 0
    j := m-1

    for i < n && j >= 0 {
        if matrix[i][j] == target {
            return true
        }

        if matrix[i][j] > target {
            j--
        } else {
            i++
        }
    }

    return false
}
```
