
`406. 根据身高重建队列` https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode-sol/
- 方法一：从低到高考虑
- 方法二：从高到低考虑

# 测试用例

```
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
[[8,0],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
[[4,0],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
```

# `000406.py`

这个实现和答案两种实现都不一样。这里先按照每个元组第二个元素排序，然后再按每个元组第一个元素排序。对于输入`[[4,0],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`，排序完成后为`[[4, 0], [5, 0], [7, 0], [6, 1], [7, 1], [5, 2], [4, 4]]`。然后对排序过后的新数组进行for循环，逐个往res里找对位置插入，整个过程res的值如下：
```
# 初始时res为空列表
[]

# 前三个第二元素为0的元组直接贴进去。
[[4,0],[5,0],[7,0]]

# 插入[6,1]  -->  找到[7,0]后面的位置插入即可。
[[4,0],[5,0],[7,0],[6,1]]

# 插入[7,1]  -->  这个和插入[6,1]不一样，按理说会先找到[7,0]后面的位置，但是不能直接插入，因为会影响[6,1]。
# 正确的做法是继续往后走，直到res的末尾或者res里下一个元素的第一个值比待插入的元素的第一个值大。
[[4,0],[5,0],[7,0],[6,1],[7,1]]

# [5,2]和[4,4]的插入和[6,1]类似，省略。

# 最终结果
[[4,0],[5,0],[7,0],[5,2],[4,4],[6,1],[7,1]]
```
