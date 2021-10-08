<!-- omit in toc -->
# 剑指 Offer 40.  最小的k个数

- Difficulty: Easy
- Topics: `Array`, `Divide and Conquer`, `Quickselect`, `Sorting`, `Heap`
- Link: https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Sorting](#sorting)
    - [Go](#go)
  - [Heap](#heap)
  - [Quick Sort](#quick-sort)
  - [Binary Search Tree](#binary-search-tree)

## Description

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


示例 1：

```
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```
示例 2：
```
输入：arr = [0,1,2,1], k = 1
输出：[0]
```

限制：

- `0 <= k <= arr.length <= 10000`
- `0 <= arr[i] <= 10000`


## Solution

### Sorting

顾名思义，求最小的 k 个数，将数组进行排序，返回前 k 个元素即可。

#### Go

- 执行用时: 36 ms
- 内存消耗: 6.5 MB

```go
func getLeastNumbers(arr []int, k int) []int {
    if k == 0 {
        return []int{}
    }

    sort.Sort(sort.IntSlice(arr))
    return arr[:k]
}
```

### Heap

TODO: 大根堆 https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/zui-xiao-de-kge-shu-by-leetcode-solution/

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/#%E4%BA%8C%E3%80%81%E5%A4%A7%E6%A0%B9%E5%A0%86%E5%89%8D-k-%E5%B0%8F-/-%E5%B0%8F%E6%A0%B9%E5%A0%86%EF%BC%88%E5%89%8D-k-%E5%A4%A7,java%E4%B8%AD%E6%9C%89%E7%8E%B0%E6%88%90%E7%9A%84-priorityqueue%EF%BC%8C%E5%AE%9E%E7%8E%B0%E8%B5%B7%E6%9D%A5%E6%9C%80%E7%AE%80%E5%8D%95%EF%BC%9A

### Quick Sort

TODO: 快排思想 https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/zui-xiao-de-kge-shu-by-leetcode-solution/

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/#%E4%B8%80%E3%80%81%E7%94%A8%E5%BF%AB%E6%8E%92%E6%9C%80%E6%9C%80%E6%9C%80%E9%AB%98%E6%95%88%E8%A7%A3%E5%86%B3-topk-%E9%97%AE%E9%A2%98%EF%BC%9A

### Binary Search Tree

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/#%E4%B8%89%E3%80%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B9%9F%E5%8F%AF%E4%BB%A5-%E8%A7%A3%E5%86%B3-topk-%E9%97%AE%E9%A2%98%E5%93%A6