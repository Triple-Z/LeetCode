<!-- omit in toc -->
# 剑指 Offer 15.  二进制中1的个数

- Difficulty: Easy
- Topics: `Bit Manipulation`
- Link: https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Iteration](#iteration)
    - [Go](#go)
  - [Brian-Kernighan Algorithm](#brian-kernighan-algorithm)
    - [Go](#go-1)

## Description

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

提示：

- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
- 在 Java 中，编译器使用 二进制补码 记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。


示例 1：
```
输入：n = 11 (控制台输入 00000000000000000000000000001011)
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
```
示例 2：
```
输入：n = 128 (控制台输入 00000000000000000000000010000000)
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
```
示例 3：
```
输入：n = 4294967293 (控制台输入 11111111111111111111111111111101，部分语言中 n = -3）
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```

提示：
- 输入必须是长度为 `32` 的 二进制串 。

注意：本题与 [191 题](./191.%20Number%20of%201%20Bits%20位1的个数.md) 相同。

## Solution

### Iteration

获取第 `i` 位比特的方法：`num & (1 << i)` 。

遍历 32 位比特，若第 `i` 位比特为 `1` ，则累加得出结果。

#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func hammingWeight(num uint32) int {
    ans := 0
    for i := 0; i < 32; i++ {
        if num & (1 << i) != 0 {
            // Ith bit is ONE
            ans++
        }
    }

    return ans
}
```

### Brian-Kernighan Algorithm

Brian-Kernighan 算法：对于任意的数字 n，其和 n-1 进行 *位与* 操作后得到的结果会将 n 中的 *最后一个* 1 变为 0 。如下图所示。

![image.png](assets/191.%20Number%20of%201%20Bits%20%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0/abfd6109e7482d70d20cb8fc1d632f90eacf1b5e89dfecb2e523da1bcb562f66-image.png)

时间复杂度为 O(1)，空间复杂度为 O(1)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func hammingWeight(num uint32) int {
    ans := 0
    for num != 0 {
        num &= num - 1
        ans++
    }

    return ans
}
```
