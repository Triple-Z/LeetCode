<!-- omit in toc -->
# Stack

- [Problems](#problems)
- [Statistics](#statistics)

## Problems

| # | Title | Solution | Difficulty | Topics | Doc |
|:----:|:----:|:----:|:----:|:----:|:----:|
| [<span id="problem-20">20</span>](#problem-20 "#20") | [Valid Parentheses <br>有效的括号](https://leetcode-cn.com/problems/valid-parentheses/ "https://leetcode-cn.com/problems/valid-parentheses/") | [Java](../../java/src/20.%20ValidParentheses.java "java/src/20.%20ValidParentheses.java") [Python3](../../py3/20.py "py3/20.py") | Easy | `Stack`, `String` | [:page_facing_up:](../../docs/20.%20Valid%20Parentheses%20%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.md "docs/20.%20Valid%20Parentheses%20%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.md") |
| [<span id="problem-94">94</span>](#problem-94 "#94") | [Binary Tree Inorder Traversal <br>二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/ "https://leetcode-cn.com/problems/binary-tree-inorder-traversal/") | [Java](../../java/src/94.%20BinaryTreeInorderTraversal.java "java/src/94.%20BinaryTreeInorderTraversal.java") [Python3](../../py3/94.py "py3/94.py") | Medium | `Hash Table`, `Stack`, `Tree` | [:page_facing_up:](../../docs/94.%20Binary%20Tree%20Inorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.md "docs/94.%20Binary%20Tree%20Inorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.md") |
| [<span id="problem-103">103</span>](#problem-103 "#103") | [Binary Tree Zigzag Level Order Traversal <br>二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/ "https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/") | [Java](../../java/src/103.%20BinaryTreeZigzagLevelOrderTraversal.java "java/src/103.%20BinaryTreeZigzagLevelOrderTraversal.java") | Medium | `Stack`, `Tree`, `Breadth-First Search` | [:page_facing_up:](../../docs/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%94%AF%E9%BD%BF%E5%BD%A2%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.md "docs/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%94%AF%E9%BD%BF%E5%BD%A2%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.md") |
| [<span id="problem-144">144</span>](#problem-144 "#144") | [Binary Tree Preorder Traversal <br>二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/ "https://leetcode-cn.com/problems/binary-tree-preorder-traversal/") | [Java](../../java/src/144.%20BinaryTreePreorderTraversal.java "java/src/144.%20BinaryTreePreorderTraversal.java") | Medium | `Stack`, `Tree` | [:page_facing_up:](../../docs/144.%20Binary%20Tree%20Preorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.md "docs/144.%20Binary%20Tree%20Preorder%20Traversal%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.md") |
| [<span id="problem-150">150</span>](#problem-150 "#150") | [Evaluate Reverse Polish Notation <br>逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/ "https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/") | [Java](../../java/src/150.%20EvaluateReversePolishNotation.java "java/src/150.%20EvaluateReversePolishNotation.java") | Medium | `Stack` | [:page_facing_up:](../../docs/150.%20Evaluate%20Reverse%20Polish%20Notation%20%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.md "docs/150.%20Evaluate%20Reverse%20Polish%20Notation%20%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.md") |
| [<span id="problem-155">155</span>](#problem-155 "#155") | [Min Stack <br>最小栈](https://leetcode-cn.com/problems/min-stack/ "https://leetcode-cn.com/problems/min-stack/") | [Java](../../java/src/155.%20MinStack.java "java/src/155.%20MinStack.java") [Python3](../../py3/155.py "py3/155.py") | Easy | `Stack`, `Design` | [:page_facing_up:](../../docs/155.%20Min%20Stack%20%E6%9C%80%E5%B0%8F%E6%A0%88.md "docs/155.%20Min%20Stack%20%E6%9C%80%E5%B0%8F%E6%A0%88.md") |
| [<span id="problem-剑指-Offer-06">剑指 Offer 06</span>](#problem-剑指-Offer-06 "#剑指 Offer 06") | [从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/ "https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_06.go "go/src/%E5%89%91%E6%8C%87_Offer_06.go") | Easy | `Stack`, `Recursion`, `Linked List`, `Two Pointers` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2006.%20%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2006.%20%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.md") |
| [<span id="problem-剑指-Offer-09">剑指 Offer 09</span>](#problem-剑指-Offer-09 "#剑指 Offer 09") | [用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/ "https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_09.go "go/src/%E5%89%91%E6%8C%87_Offer_09.go") | Easy | `Stack`, `Design`, `Queue` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2009.%20%E7%94%A8%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.md "docs/%E5%89%91%E6%8C%87%20Offer%2009.%20%E7%94%A8%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.md") |
| [<span id="problem-剑指-Offer-30">剑指 Offer 30</span>](#problem-剑指-Offer-30 "#剑指 Offer 30") | [包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/ "https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/") |  [Go](../../go/src/%E5%89%91%E6%8C%87_Offer_30.go "go/src/%E5%89%91%E6%8C%87_Offer_30.go") | Easy | `Stack`, `Design` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2030.%20%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88.md "docs/%E5%89%91%E6%8C%87%20Offer%2030.%20%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88.md") |
| [<span id="problem-剑指-Offer-36">剑指 Offer 36</span>](#problem-剑指-Offer-36 "#剑指 Offer 36") | [二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/ "https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/") | [Java](../../java/src/%E5%89%91%E6%8C%87_Offer_36.java "java/src/%E5%89%91%E6%8C%87_Offer_36.java") | Medium | `Stack`, `Tree`, `Depth-First Search`, `Binary Search Tree`, `Linked List`, `Binary Tree`, `Doubly-Linked List` | [:page_facing_up:](../../docs/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.md "docs/%E5%89%91%E6%8C%87%20Offer%2036.%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.md") |


## Statistics

- Total solved problems : 10
- Total docs : 10

Group by solution language:
- Total solutions via Java : 7
- Total solutions via Go : 3
- Total solutions via Python3 : 3
- Total solutions via C++ : 0

Group by difficulty:
- Easy: 5
- Medium: 5
- Hard: 0