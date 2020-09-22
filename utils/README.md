# Utils

仓库小工具。

### Update README

[update_readme.py](update_readme.py)

更新根目录 `README.md` 中的问题列表工具。并在其中生成解答代码和题解的链接，自动生成新的 `README.md` 文件。

使用 [Jinja2](https://github.com/pallets/jinja) 模版引擎渲染而成。并用正则匹配各个文件名，生成对应链接。

C++ 文件的正则：
```regex
cpp\/src\/(\d+)\.cpp
```

Java 文件的正则：
```regex
java\/src\/(\d+)\. \w+\.java
```

Python 文件的正则：
```regex
py3\/(\d+)\.py
```

题解文件的正则：
```regex
docs\/(\d+)\. ([\w\d\s\(\)]+)(\s+[\u4e00-\u9fa5][\u4e00-\u9fa5\w\d\s\(\)]+)?\.md
```

题解文件中题目难度和信息的正则：
```regex
- Difficulty: (Easy|Medium|Hard)\n- Topics: (`[`\w\d\s\,\-]+`)\n- Link: ((?:http|https):\/\/.*)\n
```