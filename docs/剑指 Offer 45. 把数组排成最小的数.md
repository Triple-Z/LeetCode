<!-- omit in toc -->
# 剑指 Offer 45.  把数组排成最小的数

- Difficulty: Medium
- Topics: `Greedy`, `String`, `Sorting`
- Link: https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Custom Sort](#custom-sort)
    - [Go](#go)

## Description

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

```
输入: [10,2]
输出: "102"
```
示例 2:
```
输入: [3,30,34,5,9]
输出: "3033459"
```

提示:

- `0 < nums.length <= 100`

说明:

- 输出结果可能非常大，所以你需要返回一个字符串而不是整数
- 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0


## Solution

### Custom Sort

此题其实是需要找到一种排序规则，让数组基于此规则排成一个最小的数字。

排序规则即要两两比较数值，我们如何设置排序规则才能让数组最后的值最小呢？

根据题意，数字会被转化为字符串拼接起来，因此给出 `[m, n]` 会变为 `"mn"`，当然也可能成为 `"nm"`。那么，我们只需要确定 `"mn"` 和 `"nm"` 的大小，就能够决定 `m` 和 `n` 的具体位置了。

假如 `"nm"` 小于 `"mn"` ，则排序则应为 `[n, m]`。而对于 `"nm"` 和 `"mn"` 的比较，使用字符串比较即可。

因此可以先将数字转化为字符串（解决大数比较问题），并设立以下排序规则：
- `"a" + "b" < "b" + "a"` ，则 `a < b`。
- `"a" + "b" == "b" + "a"` ，则 `a == b`。
- `"a" + "b" > "b" + "a"`，则 `a > b`。

实现该排序规则，借助不同语言的自定义排序能力即可完成。

该方法的时间复杂度为 O(nlogn)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2.4 MB

```go
func minNumber(nums []int) string {
    strs := make([]string, len(nums))
    for i := 0; i < len(nums); i++ {
        strs[i] = strconv.Itoa(nums[i])
    }

    sort.Slice(strs, func(i, j int) bool {
        if strings.Compare(strs[i] + strs[j], strs[j] + strs[i]) == -1 {
            return true
        }
        return false
    })

    builder := strings.Builder{}
    for _, s := range strs {
        builder.WriteString(s)
    }

    return builder.String()
}


```
