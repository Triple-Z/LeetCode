<!-- omit in toc -->
# 剑指 Offer 38.  字符串的排列

- Difficulty: Medium
- Topics: `String`, `Backtracking`
- Link: https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Backtrack (With Duplication)](#backtrack-with-duplication)
    - [Go](#go)
  - [Backtrack](#backtrack)
  - [Next Permutation](#next-permutation)

## Description

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 

示例:
```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```

限制：

- `1 <= s 的长度 <= 8`

## Solution

### Backtrack (With Duplication)

Permutation 就是最经典的回溯题，一定要会。

对于整个字符串的全排列，我们可以认为是两个步骤：
1. 求出所有可能出现在第一个位置的字符，即将第一个位置的字符和其他值相交换。
2. 将第一个字符固定，求后面所有字符的全排列。

第二个步骤可以看出就是一个递归过程，但我们需要在交换位置前恢复当前层原本的状态，也就是回溯。

遍历交换的过程如下：
```
s = "abcd"

i = 0, a | b c d
i = 1, b | a c d
i = 2, c | a b d
i = 3, d | a b c
```

当「后面字符」为空时，当前的结果就是一个排列，我们可以将其加入结果中。由于结果不能够重复，还需要额外去重后再将结果返回。

该方法的时间复杂度为 O(n * n!)，空间复杂度为 O(n)。

#### Go

执行用时: 72 ms
内存消耗: 9.1 MB

```go
func permutation(s string) []string {
    ansMap := make(map[string]bool)  // for remove duplication

    if len(s) == 1 {
        return []string{s}
    }

    var permutationCore func(string, string)
    permutationCore = func (cur string, remain string) {
        if len(remain) == 0 {
            ansMap[cur] = true
        }

        for i := 0; i < len(remain); i++ {
            // don't change cur/remain for backtrack
            newCur := cur + string(remain[i])
            newRemain := remain[:i] + remain[i+1:]

            permutationCore(newCur, newRemain)
        }
    }

    permutationCore("", s)

    ans := []string{}
    for permuteStr, _ := range ansMap {
        ans = append(ans, permuteStr)
    }

    return ans
}
```

### Backtrack

TODO： 直接去重的回溯 

https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-hhvs/
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/

### Next Permutation

TODO：下一个全排列 

https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-hhvs/
