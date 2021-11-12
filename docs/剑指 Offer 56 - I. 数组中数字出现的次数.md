<!-- omit in toc -->
# 剑指 Offer 56 - I.  数组中数字出现的次数

- Difficulty: Medium
- Topics: `Bit Manipulation`, `Array`
- Link: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Grouping XOR](#grouping-xor)
    - [Go](#go)

## Description

一个整型数组 `nums` 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。


示例 1：
```
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
```
示例 2：
```
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
```

限制：

- `2 <= nums.length <= 10000`


## Solution

### Grouping XOR

如果题目内容是「在一个数字都出现两次的数组中，求一个只出现一次的数字」，就会很简单了，因为只需要将所有数字遍历按位异或一遍，即可得出那个只出现一次的数字（原因是 `a ^ a = 0` 和 `0 ^ a = a`）。

但是题目中的条件是：有两个数字都只出现一次。这可怎么办呢？事实上，我们已经知道了如何在一个数组中挑选出只出现一次的数字，那要是我们能将数组的值分成两组，保证两组中都只有一个数字只出现一次，就可以解决这个问题。

所以现在的问题变成了：如何将这个数组分为两组，保证每组的数字中只有一个只出现一次的数值？没错，最后的方法就是「分组异或」。

假设各只出现一次的两个数字为 `a` 和 `b` ，我们可以得知，`a ^ b != 0` 。而 `a` 和 `b` 异或的二进制结果，若某个二进位 `i` 的值为 `1` ，则代表在该位上，`a(i)` 和 `b(i)` 的值刚好不同。为了方便起见，笔者直接选用了从低位到高位方向的第一个二进制 `1` 作为目标二进制位。

那就可以用目标二进制位来作为两组数据的分配依据：若数组中数字的第 `i` 个二进位为 `1`，则将该数字分配值第一组中，否则分配到第二组。两组数字分别遍历做异或操作，分别得到的结果，即为我们希望得到的两个数字。

此方法的时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 16 ms
- 内存消耗: 6.3 MB

```go
func singleNumbers(nums []int) []int {
    t := 0
    for i := 0; i < len(nums); i++ {
        t ^= nums[i]
    }

    mask := 1
    for (mask & t) == 0 {
        mask <<= 1
    }

    num1, num2 := 0, 0
    for i := 0; i < len(nums); i++ {
        if (nums[i] & mask) != 0 {
            // the target position of num[i] is 1
            num1 ^= nums[i]
        } else {
            // the target position of num[i] is 0
            num2 ^= nums[i]
        }
    }

    return []int{num1, num2}
}
```
