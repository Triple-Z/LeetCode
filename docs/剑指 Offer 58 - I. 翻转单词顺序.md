<!-- omit in toc -->
# 剑指 Offer 58 - I.  翻转单词顺序

- Difficulty: Easy
- Topics: `Two Pointers`, `String`
- Link: https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [String Library](#string-library)
    - [Go](#go)
  - [Two Pointers](#two-pointers)
    - [Go](#go-1)

## Description

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：
```
输入: "the sky is blue"
输出: "blue is sky the"
```
示例 2：
```
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
```
示例 3：
```
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
```

说明：
- 无空格字符构成一个单词。
- 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
- 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


## Solution

### String Library

如果能够使用标准库中的字符串处理函数，那一切都变得简单了。

翻转单词顺序可以分为以下两个步骤：
1. 先将单词按照 `" "` 切分成字符串数组。
2. 从后往前遍历该字符串数组。
3. 遍历若遇到非空字符串，则将其添加到结果字符串中。

时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 3.8 MB

```go
func reverseWords(s string) string {
    words := strings.Split(s, " ")
    ans := strings.Builder{}
    first := true
    for i := len(words)-1; i >= 0; i-- {
        if words[i] != "" {
            if !first {
                ans.WriteString(" ")
            } else {
                first = false
            }
            ans.WriteString(strings.Trim(words[i], " "))
        }
    }

    return ans.String()
}
```

### Two Pointers

由于单词需要逆序，因此我们先将两指针都置于字符串尾部，其中左指针用于查找单词的起始字符位置，右指针用于查找单词的结尾字符位置，当两指针找到单词后，即可加入结果字符串中。

需要注意最后一个单词的处理，此时左指针已越界，可以用 `[0:j+1]` 来取字符串。

此方法时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 3.7 MB

```go
func reverseWords(s string) string {
    i, j := len(s)-1, len(s)-1
    // traverse backward
    b := strings.Builder{}
    first := true
    for i >= 0 {
        if s[j] == byte(' ') {
            j--
            i = j
            continue
        }
        if s[i] != byte(' ') {
            i--
            continue
        }
        // get a word
        if first {
            first = false
        } else {
            b.WriteString(" ")
        }
        b.WriteString(s[i+1:j+1])
        j = i
    }

    if i == -1 && i != j {
        if first {
            first = false
        } else {
            b.WriteString(" ")
        }
        b.WriteString(s[i+1:j+1])
    }

    return b.String()
}
```