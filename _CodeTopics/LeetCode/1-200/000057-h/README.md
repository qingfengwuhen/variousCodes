
`57. 插入区间` https://leetcode-cn.com/problems/insert-interval/solution/cha-ru-qu-jian-by-leetcode-solution/
- [x] 方法一：模拟

# 测试用例

```
[[1,3],[6,9]]
[2,5]
[[1,3],[6,9]]
[5,7]
[[1,3],[6,9]]
[2,7]
[[1,3],[6,9]]
[4,5]
[[1,2],[3,5],[6,7],[8,10],[12,16]]
[4,8]
[]
[5,7]

# 该用例不合法，因为初始的intervals里的区间无交集。但是，可以用来测一些更一般的情况：
# 比如初始时区间之间可以有交集（但是，仍按照每个区间左边的那个数的大小顺序排列）
[[1,2],[3,11],[6,7],[8,10],[12,16]]
[4,8]

# 下面这俩输入，官方也没有输出，所以是不符合要求的输入。也就是输入newInterval不会是空集。
[]
[]
[[1,2]]
[]
```
