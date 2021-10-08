<!-- omit in toc -->
# 剑指 Offer 61.  扑克牌中的顺子

- Difficulty: Easy
- Topics: `Array`, `Sorting`
- Link: https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/

- [Description](#description)
- [Solution](#solution)
  - [Sorting](#sorting)
    - [Go](#go)
  - [Hash Table](#hash-table)
    - [Go](#go-1)

## Description

从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:
```
输入: [1,2,3,4,5]
输出: True
```

示例 2:
```
输入: [0,0,1,2,5]
输出: True
```

限制：

数组长度为 5 

数组的数取值为 `[0, 13]` .


## Solution

### Sorting

先遍历数组，获得大小王的个数（即任意数字的个数），以及除大小王外的最大最小值。

按照题意，每次随机抽取 5 张牌，因此这五张牌中若最大最小值相差大于 5，则肯定不能组成顺子，可以直接返回 `false` 。相应地，若五张牌都为大小王，则直接返回 `true` 。

接着，对 `nums` 进行从小到大的排序，在排序的结果中，`0` 一定在最前面，因此我们可以将 `0` 跳过。当找到第一个非零数字时，开始记录该值，并计算下一个值成为“顺子”的期望值（即 `num[i]+1`）。若下一个值不符合期望，则需要看当前是否还有大小王能够补齐该值，若无则说明这组牌中没有顺子，否则可以继续判断，最后循环结束则证明牌都合法，可组成顺子。

根据以上的思路，可以直接简化成一轮循环。先对牌组进行排序，从小到大遍历，获取到大小王（`0` 值）的个数后，下一个值就是顺子开始的最小值，如此判断下去即可得到结果。

此方法时间复杂度为 O(n)，空间复杂度为 O(1)。

#### Go

先找 min/max 再循环找顺子。

- 执行用时: 0 ms
- 内存消耗: 2016 KB

```go
func isStraight(nums []int) bool {
    kings := 0
    min := 14
    max := 0
    for _, num := range nums {
        if num == 0 {
            // king
            kings++
        } else {
            if num < min {
                min = num
            }
            if num > max {
                max = num
            }
        }
    }

    if kings == 5 {
        // all kings
        return true
    }

    if max - min >= 5 {
        return false
    }

    sort.Sort(sort.IntSlice(nums))
    j := 0
    for _, num := range nums {
        if num != 0 {
            break
        }
        j++
    }

    next := min
    for i := j; i < 5; i++ {
        // fmt.Println(next)
        if nums[i] != next && kings > 0 {
            // fmt.Println("kings--")
            kings--
            next++
            i--
            continue
        } else if nums[i] != next && kings == 0 {
            return false
        }
        next++
    }

    return true
}
```

简化，一轮循环。

- 执行用时: 0 ms
- 内存消耗: 2020 KB

```go
func isStraight(nums []int) bool {
    sort.Sort(sort.IntSlice(nums))

    kings := 0
    next := -1
    for i := 0; i < 5; i++ {
        if nums[i] == 0 {
            kings++
            continue
        } else if next == -1 {
            // first shunzi
            next = nums[i]
        }

        if nums[i] != next && kings > 0 {
            kings--
            next++
            i--
            continue
        } else if nums[i] != next && kings == 0 {
            return false
        }
        next++
    }

    return true
}
```

### Hash Table

顺着 Sort 的思路，其实只要通过 `max - min < 5` 且元素（除大小王外）不重复即可判断出是否能够存在顺子。去重的过程很自然通过一个哈希表来实现，此法时间复杂度为 O(n)，空间复杂度为 O(n)。

#### Go

- 执行用时: 0 ms
- 内存消耗: 2016 KB

```go
func isStraight(nums []int) bool {
    nMap := make(map[int]bool)
    nMin := 14
    nMax := -1

    for i := 0; i < 5; i++ {
        if nums[i] == 0 {
            continue
        }
        if _, ok := nMap[nums[i]]; ok {
            // duplicate
            return false
        }
        nMap[nums[i]] = true
        nMax = max(nMax, nums[i])
        nMin = min(nMin, nums[i])
    }

    return nMax - nMin < 5
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```