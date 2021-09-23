<!-- omit in toc -->
# 剑指 Offer 05.  替换空格

- Difficulty: Easy
- Topics: `String`
- Link: https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Build a String](#build-a-string)
    - [Go](#go)

## Description

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


示例 1：
```
输入：s = "We are happy."
输出："We%20are%20happy."
```

限制：
```
0 <= s 的长度 <= 10000
```

## Solution

### Build a String

遍历字符串，构建一个新的字符串，每次遇到空格，替换成 `%20`，然后把新的字符串拼接到结果字符串后面。


#### Go

- 执行用时: 0 ms
- 内存消耗: 1.9 MB

```go
func replaceSpace(s string) string {
    b := strings.Builder{}
    for _, c := range s {
        if c == ' ' {
            b.WriteString("%20")
        } else {
            b.WriteRune(c)
        }
    }

    return b.String()
}
```
