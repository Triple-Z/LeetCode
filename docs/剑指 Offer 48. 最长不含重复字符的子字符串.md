<!-- omit in toc -->
# 剑指 Offer 48.  最长不含重复字符的子字符串

- Difficulty: Medium
- Topics: `Hash Table`, `String`, `Sliding Window`
- Link: https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Sliding Window](#sliding-window)
    - [Go](#go)
  - [Dynamic Programming](#dynamic-programming)
    - [Lang](#lang)

## Description

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。


示例 1:
```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
示例 2:
```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
示例 3:
```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

提示：

- `s.length <= 40000`

## Solution

### Sliding Window

要查找不重复字符的子字符串，可以使用滑动窗口并借助哈希表来实现。

滑动窗口的策略非常重要，此题中滑动窗口的策略为：
1. 查看滑动窗口后一个值 `s[j]` 的内容是否在窗口中存在（哈希表中是否存在）。
2. 若存在，则说明当前 `[i, j)` 为一个不含重复字符的子字符串，计算该串的大小，将其加入最大值比较的内容。同时需要缩小窗口，不断将窗口左侧进行左移，直到越过窗口中原来存在与 `s[j]` 的重复值。
3. 若不存在，则将窗口扩大，将窗口右侧右移。
4. 最后需要确认窗口右侧位于尾部时的子串大小，将其加入最大值比较的内容，得出结果。

此方法时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

- 执行用时: 8 ms
- 内存消耗: 2.6 MB

```go
func lengthOfLongestSubstring(s string) int {
    if s == "" {
        return 0
    }

    cMap := make(map[byte]bool)
    i, j := 0, 1
    cMap[s[i]] = true
    maxChars := 1
    for i <= j && j < len(s) {
        if _, ok := cMap[s[j]]; ok {
            // last string: [i, j)
            maxChars = max(maxChars, j-i)
            for s[i] != s[j] {
                delete(cMap, s[i])
                i++
            }
            delete(cMap, s[i])
            i++
            continue
        }
        cMap[s[j]] = true
        j++
    }
    if j == len(s) {
        maxChars = max(maxChars, j-i)
    }

    return maxChars
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### Dynamic Programming

TODO

#### Lang

```lang
2nd solution code goes here.
```