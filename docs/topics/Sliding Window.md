<!-- omit in toc -->
# Sliding Window

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-3">3</span>](#problem-3 "#3") | [Longest Substring Without Repeating Characters <br>无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters "https://leetcode-cn.com/problems/longest-substring-without-repeating-characters") | [Java](../../java/src/3.%20LongestSubstringWithoutRepeatingCharacters.java "java/src/3.%20LongestSubstringWithoutRepeatingCharacters.java") [Go](../../go/src/3.go "go/src/3.go") [Python3](../../py3/3.py "py3/3.py") | Medium | `Hash Table`, `String`, `Sliding Window` | [:page_facing_up:](../../docs/3.%20Longest%20Substring%20Without%20Repeating%20Characters%20%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md "docs/3.%20Longest%20Substring%20Without%20Repeating%20Characters%20%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md") |
| [<span id="problem-239">239</span>](#problem-239 "#239") | [Sliding Window Maximum <br>滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/ "https://leetcode-cn.com/problems/sliding-window-maximum/") |  [Go](../../go/src/239.go "go/src/239.go") | Hard | `Queue`, `Array`, `Sliding Window`, `Monotonic Queue`, `Heap` | [:page_facing_up:](../../docs/239.%20Sliding%20Window%20Maximum%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.md "docs/239.%20Sliding%20Window%20Maximum%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.md") |
| [<span id="problem-剑指-Offer-48">剑指 Offer 48</span>](#problem-剑指-Offer-48 "#剑指 Offer 48") | [最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/ "https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_48.go "go/src/%E5%89%91%E6%8C%87_Offer_48.go") | Medium | `Hash Table`, `String`, `Sliding Window` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2048.%20%E6%9C%80%E9%95%BF%E4%B8%8D%E5%90%AB%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md "docs/%E5%89%91%E6%8C%87%20Offer%2048.%20%E6%9C%80%E9%95%BF%E4%B8%8D%E5%90%AB%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md") |
| [<span id="problem-剑指-Offer-59---I">剑指 Offer 59 - I</span>](#problem-剑指-Offer-59---I "#剑指 Offer 59 - I") | [滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/ "https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_59_-_I.go "go/src/%E5%89%91%E6%8C%87_Offer_59_-_I.go") | Hard | `Queue`, `Sliding Window`, `Monotonic Queue`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2059%20-%20I.%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC.md "docs/%E5%89%91%E6%8C%87%20Offer%2059%20-%20I.%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC.md") |


## Statistics

- Total solved problems : 4
- Total docs : 4

Group by solution language:
- Total solutions via Java : 1
- Total solutions via Go : 4
- Total solutions via Python3 : 1
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 0
- Medium: 2
- Hard: 2