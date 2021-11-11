<!-- omit in toc -->
# Binary Search Tree

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-235">235</span>](#problem-235 "#235") | [Lowest Common Ancestor of a Binary Search Tree <br>二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ "https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/") | [Java](../../java/src/235.%20LowestCommonAncestorofaBinarySearchTree.java "java/src/235.%20LowestCommonAncestorofaBinarySearchTree.java") [Go](../../go/src/235.go "go/src/235.go") | Easy | `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree` | [:page_facing_up:](../../docs/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md "docs/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md") |
| [<span id="problem-剑指-Offer-33">剑指 Offer 33</span>](#problem-剑指-Offer-33 "#剑指 Offer 33") | [二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/ "https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_33.go "go/src/%E5%89%91%E6%8C%87_Offer_33.go") | Medium | `Stack`, `Tree`, `Binary Search Tree`, `Recursion`, `Binary Tree`, `Monotonic Stack` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2033.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2033.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.md") |
| [<span id="problem-剑指-Offer-36">剑指 Offer 36</span>](#problem-剑指-Offer-36 "#剑指 Offer 36") | [二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/ "https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/") | [Java](../../java/src/%E5%89%91%E6%8C%87_Offer_36.java "java/src/%E5%89%91%E6%8C%87_Offer_36.java") | Medium | `Stack`, `Tree`, `Depth-First Search`, `Binary Search Tree`, `Linked List`, `Binary Tree`, `Doubly-Linked List` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-剑指-Offer-54">剑指 Offer 54</span>](#problem-剑指-Offer-54 "#剑指 Offer 54") | [二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/ "https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_54.go "go/src/%E5%89%91%E6%8C%87_Offer_54.go") | Easy | `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2054.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E5%A4%A7%E8%8A%82%E7%82%B9.md "docs/%E5%89%91%E6%8C%87%20Offer%2054.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E5%A4%A7%E8%8A%82%E7%82%B9.md") |
| [<span id="problem-剑指-Offer-68---I">剑指 Offer 68 - I</span>](#problem-剑指-Offer-68---I "#剑指 Offer 68 - I") | [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/ "https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/") | [Java](../../java/src/%E5%89%91%E6%8C%87_Offer_68_-_I.java "java/src/%E5%89%91%E6%8C%87_Offer_68_-_I.java") [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_68_-_I.go "go/src/%E5%89%91%E6%8C%87_Offer_68_-_I.go") | Easy | `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2068%20-%20I.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md "docs/%E5%89%91%E6%8C%87%20Offer%2068%20-%20I.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.md") |


## Statistics

- Total solved problems : 5
- Total docs : 5

Group by solution language:
- Total solutions via Java : 3
- Total solutions via Go : 4
- Total solutions via Python3 : 0
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 3
- Medium: 2
- Hard: 0