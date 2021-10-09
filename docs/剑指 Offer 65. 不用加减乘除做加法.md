<!-- omit in toc -->
# 剑指 Offer 65.  不用加减乘除做加法

- Difficulty: Easy
- Topics: `Bit Manipulation`, `Math`
- Link: https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Simulation](#simulation)
    - [Go](#go)
  - [Bit Manipulation](#bit-manipulation)
    - [Go](#go-1)

## Description

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
```
输入: a = 1, b = 1
输出: 2
```

提示：

- `a`, `b` 均可能是负数或 0
- 结果不会溢出 32 位整数

## Solution

### Simulation

笔者首先想到的是数字电路的模拟方法。众所周知，计算机内有符号负整数的存储方式是补码，因此负数与正数的加法可以直接相加，若结果为正，则符号位的结果会自然溢出，例子如下：

```
    1 1 0 1   (-3)
 +  0 1 1 0   ( 6)
------------
(1) 0 0 1 1   ( 3)
```

> 结果中最高位 `1` 自然溢出，因此结果为 `0011` ，十进制为 `3` 。

如何获得第 n 位上的比特位数值呢？可以借助一个位掩码和位运算操作实现。例如，获取变量 `a` 的第 `n` 位的值为：

```go
aNthBit := a & (1 << n)
```

`1 << n` 即为位掩码，和 `a` 按位与后得到的结果的第 n 位为 `a` 第 n 位内容，其余位上全为 `0` 。

考虑到两者之和，以及进位，我们能够得到状态表如下：

| a Nth bit | b Nth bit | ci (Carry In) | result Nth bit | ci (Next Carry In) |
|:----|:----|:----|----:|----:|
|0|0|0|0|0|
|0|1|0|1|0|
|1|0|0|1|0|
|1|1|0|0|1|
|0|0|1|1|0|
|0|1|1|0|1|
|1|0|1|0|1|  
|1|1|1|1|1|

还有一个问题需要解决，那就是如何对结果变量的第 n 位进行赋值 `0` 或 `1` ？答案还是通过位操作，方法如下表：

|| Bit Operation | Example |
|----|:----:|:----:|
|Set Nth bit to `0` | AND NOT | `ans &^= (1 << n)` |
|Set Nth bit to `1` | OR | `ans \|= (1 << n)` |

剩下的工作就是根据状态表对结果按位赋值即可。

#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func add(a int, b int) int {
    ci := 0
    mask := 1
    ans := 0
    
    for i := 0; i < 64; i++ {
        aBit := a & mask
        bBit := b & mask

        if ci == 0 {
            if aBit ^ bBit == 0 {
                if aBit != 0 {
                    // 1 and 1
                    ci = 1
                }
                ans &^= mask // set bit zero
            } else {
                // 0 and 1
                ans |= mask // set bit one
            }
        } else { // carry in
            ci = 0
            if aBit ^ bBit == 0 {
                if aBit != 0 {
                    // 1 and 1 and 1
                    ci = 1
                }
                ans |= mask // set bit one
            } else {
                // 0 and 1 and 1
                ci = 1
                ans &^= mask // set bit zero
            }
        }
        mask <<= 1
    }

    return ans
}
```

### Bit Manipulation

> 参考 [@Krahets 的题解](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)。

设两数字的二进制形式 `a`, `b` ，其求和 `s = a + b`，`a(i)` 代表 `a` 的二进制第 `i` 位，则分为以下四种情况：

| `a(i)`	| `b(i)` | 无进位和 `n(i)`	| 进位 `c(i+1)` |
|----|----|----|-----|
| 0	| 0	| 0	| 0 |
| 0	| 1	| 1	| 0 |
| 1	| 0	| 1	| 0 |
| 1	| 1	| 0	| 1 |

其中「无进位和」与异或运算（XOR）规律相同，「进位」与运算（AND）规律相同（并需左移一位）。

因此目前可得到以下结论：
- 无进位和：`n = a ^ b`
- 进位结果：`c = (a & b) << 1`

而「无进位和」与「进位结果」之和，又为最终结果。

我们这里仍以 `-3` 和 `6` 为例。

```
    1 1 0 1   (-3)
 +  0 1 1 0   ( 6)
------------
(1) 0 0 1 1   ( 3)

    1 0 1 1   (-3 ^ 6, -3+6 的无进位和)
 +  1 0 0 0   (-3 & 6 << 1, -3+6 的进位结果)
------------
(1) 0 0 1 1   ( 3)
```

可见，`a + b = (a ^ b) + (a & b << 1)` 成立。

但是依照题意，我们不能使用加法。而得到的转换式中又包含加法，那自然就想到了递归/迭代的方法：注意其退出条件为「进位为 0，返回无进位和」，即 `(a & b) << 1 == 0` 。

#### Go

递归解法，当进位不为零时，继续计算「无进位和」与「进位结果」的加法。

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func add(a int, b int) int {
    if a & b << 1 == 0 {
        return a ^ b
    }

    return add(a ^ b, a & b << 1)
}
```

迭代解法，当进位不为零时，继续计算「无进位和」与「进位结果」，并换位继续执行加法操作。

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func add(a int, b int) int {
    var sum, ci int
    for b != 0 {
        sum = a ^ b
        ci = a & b << 1
        a, b = sum, ci
    }
    return a
}
```
