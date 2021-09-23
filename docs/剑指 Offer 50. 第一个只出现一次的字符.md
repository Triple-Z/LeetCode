<!-- omit in toc -->
# 剑指 Offer 50.  第一个只出现一次的字符

- Difficulty: Easy
- Topics: `Queue`, `Hash Table`, `String`, `Counting`
- Link: https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Hash Table](#hash-table)
    - [Go](#go)
  - [Queue](#queue)

## Description

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
```
输入：s = "abaccdeff"
输出：'b'
```
示例 2:
```
输入：s = "" 
输出：' '
```

限制：
```
0 <= s 的长度 <= 50000
```


## Solution

### Hash Table

先遍历一遍，将内容在哈希表中进行累加计数，同时当遇到新字符时，也将字符加入列表中，实现一个“有序哈希表”。

最后通过遍历字符顺序列表，找到首个出现次数为 1 的字符，直接返回即可。

#### Go

- 执行用时: 52 ms
- 内存消耗: 5.4 MB

```go
func firstUniqChar(s string) byte {
    cMap := make(map[byte]int)
    order := []byte{}

    for i := 0; i < len(s); i++ {
        if last, ok := cMap[s[i]]; ok {
            cMap[s[i]] = last + 1
        } else {
            order = append(order, s[i])
            cMap[s[i]] = 1
        }
    }

    for _, c := range order {
        if cMap[c] == 1 {
            return c
        }
    }

    return byte(' ')
}
```

### Queue

TODO: https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-by-3zqv5/
