<!-- omit in toc -->
# Heap

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-215">215</span>](#problem-215 "#215") | [Kth Largest Element in an Array <br>数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/ "https://leetcode-cn.com/problems/kth-largest-element-in-an-array/") | [Java](../../java/src/215.%20KthLargestElementinanArray.java "java/src/215.%20KthLargestElementinanArray.java") | Medium | `Heap`, `Divide and Conquer` | [:page_facing_up:](../../docs/215.%20Kth%20Largest%20Element%20in%20an%20Array%20%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E7%AC%ACK%E4%B8%AA%E6%9C%80%E5%A4%A7%E5%85%83%E7%B4%A0.md "docs/215.%20Kth%20Largest%20Element%20in%20an%20Array%20%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E7%AC%ACK%E4%B8%AA%E6%9C%80%E5%A4%A7%E5%85%83%E7%B4%A0.md") |
| [<span id="problem-239">239</span>](#problem-239 "#239") | [Sliding Window Maximum <br>滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/ "https://leetcode-cn.com/problems/sliding-window-maximum/") |  [Go](../../go/src/239.go "go/src/239.go") | Hard | `Queue`, `Array`, `Sliding Window`, `Monotonic Queue`, `Heap` | [:page_facing_up:](../../docs/239.%20Sliding%20Window%20Maximum%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.md "docs/239.%20Sliding%20Window%20Maximum%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.md") |
| [<span id="problem-264">264</span>](#problem-264 "#264") | [Ugly Number II <br>丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/ "https://leetcode-cn.com/problems/ugly-number-ii/") |  [Go](../../go/src/264.go "go/src/264.go") | Medium | `Hash Table`, `Math`, `Dynamic Programming`, `Heap` | [:page_facing_up:](../../docs/264.%20Ugly%20Number%20II%20%E4%B8%91%E6%95%B0%20II.md "docs/264.%20Ugly%20Number%20II%20%E4%B8%91%E6%95%B0%20II.md") |
| [<span id="problem-295">295</span>](#problem-295 "#295") | [Find Median from Data Stream <br>数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/ "https://leetcode-cn.com/problems/find-median-from-data-stream/") |  [Go](../../go/src/295.go "go/src/295.go") | Hard | `Design`, `Two Pointers`, `Data Stream`, `Sorting`, `Heap` | [:page_facing_up:](../../docs/295.%20Find%20Median%20from%20Data%20Stream%20%E6%95%B0%E6%8D%AE%E6%B5%81%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.md "docs/295.%20Find%20Median%20from%20Data%20Stream%20%E6%95%B0%E6%8D%AE%E6%B5%81%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.md") |
| [<span id="problem-347">347</span>](#problem-347 "#347") | [Top K Frequent Elements <br>前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/ "https://leetcode-cn.com/problems/top-k-frequent-elements/") | [Java](../../java/src/347.%20TopKFrequentElements.java "java/src/347.%20TopKFrequentElements.java") [Python3](../../py3/347.py "py3/347.py") | Medium | `Heap`, `Hash Table` | [:page_facing_up:](../../docs/347.%20Top%20K%20Frequent%20Elements%20%E5%89%8D%20K%20%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.md "docs/347.%20Top%20K%20Frequent%20Elements%20%E5%89%8D%20K%20%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.md") |
| [<span id="problem-912">912</span>](#problem-912 "#912") | [Sort an Array <br>排序数组](https://leetcode.cn/problems/sort-an-array/ "https://leetcode.cn/problems/sort-an-array/") |  [Go](../../go/src/912.go "go/src/912.go") | Medium | `Array`, `Divide and Conquer`, `Bucket Sort`, `Counting Sort`, `Radix Sort`, `Sorting`, `Heap`, `Merge Sort` | [:page_facing_up:](../../docs/912.%20Sort%20an%20Array%20%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.md "docs/912.%20Sort%20an%20Array%20%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.md") |
| [<span id="problem-剑指-Offer-40">剑指 Offer 40</span>](#problem-剑指-Offer-40 "#剑指 Offer 40") | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/ "https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_40.go "go/src/%E5%89%91%E6%8C%87_Offer_40.go") | Easy | `Array`, `Divide and Conquer`, `Quickselect`, `Sorting`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2040.%20%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2040.%20%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-41">剑指 Offer 41</span>](#problem-剑指-Offer-41 "#剑指 Offer 41") | [数据流中的中位数](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/ "https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_41.go "go/src/%E5%89%91%E6%8C%87_Offer_41.go") | Hard | `Design`, `Two Pointers`, `Data Stream`, `Sorting`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2041.%20%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2041.%20%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-49">剑指 Offer 49</span>](#problem-剑指-Offer-49 "#剑指 Offer 49") | [丑数](https://leetcode-cn.com/problems/chou-shu-lcof/ "https://leetcode-cn.com/problems/chou-shu-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_49.go "go/src/%E5%89%91%E6%8C%87_Offer_49.go") | Medium | `Hash Table`, `Math`, `Dynamic Programming`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2049.%20%E4%B8%91%E6%95%B0.md "docs/%E5%89%91%E6%8C%87%20Offer%2049.%20%E4%B8%91%E6%95%B0.md") |
| [<span id="problem-剑指-Offer-59---I">剑指 Offer 59 - I</span>](#problem-剑指-Offer-59---I "#剑指 Offer 59 - I") | [滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/ "https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_59_-_I.go "go/src/%E5%89%91%E6%8C%87_Offer_59_-_I.go") | Hard | `Queue`, `Sliding Window`, `Monotonic Queue`, `Heap` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2059%20-%20I.%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC.md "docs/%E5%89%91%E6%8C%87%20Offer%2059%20-%20I.%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC.md") |


## Statistics

- Total solved problems : 10
- Total docs : 10

Group by solution language:
- Total solutions via Java : 2
- Total solutions via Go : 8
- Total solutions via Python3 : 1
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 1
- Medium: 5
- Hard: 4