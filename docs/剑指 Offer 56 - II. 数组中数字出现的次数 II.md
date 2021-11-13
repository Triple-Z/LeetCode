<!-- omit in toc -->
# 剑指 Offer 56 - II.  数组中数字出现的次数 II

- Difficulty: Medium
- Topics: `Bit Manipulation`, `Array`
- Link: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Hash Table](#hash-table)
    - [Go](#go)
  - [Bit Sum and Divide](#bit-sum-and-divide)
    - [Go](#go-1)

## Description

在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。


示例 1：
```
输入：nums = [3,4,3,3]
输出：4
```
示例 2：
```
输入：nums = [9,1,7,9,7,9,7]
输出：1
```

限制：

- `1 <= nums.length <= 10000`
- `1 <= nums[i] < 2^31`

## Solution

### Hash Table

简单粗暴。遍历一遍数组，给每个不同的数字单独计数。最后遍历哈希表，将数量为 1 的数字返回即可。

时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 24 ms
- 内存消耗: 6.9 MB

```go
func singleNumber(nums []int) int {
    nMap := make(map[int]int)
    for _, num := range nums {
        nMap[num] += 1
    }

    for num, cnt := range nMap {
        if cnt == 1 {
            return num
        }
    }
    return -1
}
```


### Bit Sum and Divide

顺着前两题的思路，求只出现一次的数字，用的是按位异或的方式。但是在这道题中，按位异或没办法继续用下去了。因为本题中的数组，每个数字都出现三次，无法用按位异或达到两两消除的效果。

事实上，按位异或的本质是 `(a(i) + a(i)) % 2` ，所以相应地，我们完全可以对所有的数字的某位进行累加，若该位之和能够被 3 所整除，说明只出现一次的数字该位为 0，否则为 1。用这种方法，即可拼凑出目标数字所有的二进制值，得到那个只出现一次的数字。

将指定二进制位赋值为 `1`：
```go
ans = ans | mask
```

将指定二进制位赋值为 `0`：
```go
ans = ans & (^mask)
```

此方法的时间复杂度为 O(32\*n)，即 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 32 ms
- 内存消耗: 6.5 MB

```go
func singleNumber(nums []int) int {
    bitSum := make([]int, 32)

    for i := 0; i < len(nums); i++ {
        mask := 1
        for j := 0; j < 32; j++ {
            if nums[i] & mask != 0 {
                // nums[i](j) bit is 1
                bitSum[j] += 1
            }

            mask = mask << 1
        }
    }

    mask := 1
    ans := 0
    for i := 0; i < 32; i++ {
        if bitSum[i] % 3 == 0 {
            // ans(i) bit is 0
            ans = ans & (^mask)
        } else {
            // ans(i) bit is 1
            ans = ans | mask
        }
        mask = mask << 1
    }

    return ans
}
```
