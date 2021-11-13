<!-- omit in toc -->
# 剑指 Offer 66.  构建乘积数组

- Difficulty: Medium
- Topics: `Array`, `Prefix Sum`
- Link: https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Brute-force (Time Limit Exceeded)](#brute-force-time-limit-exceeded)
    - [Go](#go)
  - [Prefix Product](#prefix-product)
    - [Go](#go-1)

## Description

给定一个数组 `A[0,1,…,n-1]`，请构建一个数组 `B[0,1,…,n-1]`，其中 `B[i]` 的值是数组 `A` 中除了下标 `i` 以外的元素的积, 即 `B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]`。不能使用除法。


示例:
```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```

提示：

- 所有元素乘积之和不会溢出 32 位整数
- `a.length <= 100000`

## Solution

### Brute-force (Time Limit Exceeded)

两重循环，对每个目标位置都计算其他位置的乘积，最后返回目标结果。

时间复杂度为 O(n^2)，空间复杂度为 O(1)。超时。

#### Go

```go
func constructArr(a []int) []int {
    b := make([]int, len(a))
    for i := 0; i < len(a); i++ {
        mul := 1
        for j := 0; j < len(a); j++ {
            if i != j {
                mul *= a[j]
            }
        }
        b[i] = mul
    }

    return b
}
```

### Prefix Product

先来看 `B[i]` 的计算方法：

```
B[i] = A[0] * A[1] * ... * A[i-1] * A[i+1] * ... * A[n-1]
```

`B[i]` 就是除去 `A[i]` 外数组 `A` 中所有元素的乘积。题目中提到不允许使用除法，否则可以先将 `A` 的所有元素乘积计算出来，再除上当前元素得到 `B[i]` 。

由于 `B[i]` 的计算中，分隔值就是 `A[i]` 。那可以将 `A[i]` 左侧的乘积和 `A[i]` 右侧的乘积拆分开来，计为 `C[i]` 和 `D[i]` ，像这样：

```
B[i] = A[0] * A[1] * ... * A[i-1] * A[i+1] * ... * A[n-1]
        \______________________/     \_________________/
                   C[i]                      D[i]

C[i] = A[0] * A[1] * ... * A[i-1]
D[i] = A[i+1] * ... * A[n-1]

B[i] = C[i] * D[i]
```

那这就成为了一个前缀积问题。只要分别将 `C[i]` 和 `D[i]` 计算出来。就可以轻松得到 `B[i]` 的值。

而 `C[i]` 和 `D[i]` 的计算方式：

```
C[0] = 1
C[1] = C[0] * A[0]
...
C[i] = C[i-1] * A[i-1]
...
C[n-1] = C[n-2] * A[n-2]

D[0] = D[1] * A[1]
D[1] = D[2] * A[2]
...
D[i] = D[i+1] * A[i+1]
...
D[n-2] = D[n-1] * A[n-1]
D[n-1] = 1
```

刚好 `C` 是前缀积，而 `D` 是后缀积。通过正反两个方向的遍历，即可得到结果。

此方法的时间复杂度为 O(n)，空间复杂度为 O(n)。

事实上，该方法的空间复杂度可以降为 O(1)。`C` 和 `D` 数组的计算过程可以直接借助结果数组 `B` 完成。

#### Go

借助 C 和 D 两个辅助数组。

- 执行用时: 24 ms
- 内存消耗: 9.9 MB

```go
func constructArr(a []int) []int {
    if len(a) < 1 {
        return []int{}
    }

    b := make([]int, len(a))
    c := make([]int, len(a)) // prefix
    d := make([]int, len(a)) // postfix

    c[0] = 1
    for i := 1; i < len(a); i++ {
        c[i] = c[i-1] * a[i-1]
    }

    d[len(d)-1] = 1
    for i := len(a)-2; i >= 0; i-- {
        d[i] = d[i+1] * a[i+1]
    }

    for i := 0; i < len(a); i++ {
        b[i] = c[i] * d[i]
    }
    
    return b
}
```

仅用 B 来实现 C 和 D 的计算。

- 执行用时: 24 ms
- 内存消耗: 9.2 MB

```go
func constructArr(a []int) []int {
    if len(a) < 1 {
        return []int{}
    }

    b := make([]int, len(a))

    b[0] = 1
    for i := 1; i < len(a); i++ {
        b[i] = b[i-1] * a[i-1]
    }

    temp := 1
    for i := len(a)-2; i >= 0; i-- {
        temp = temp * a[i+1]
        b[i] = temp * b[i]
    }
    
    return b
}
```
