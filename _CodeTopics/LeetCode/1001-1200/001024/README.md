
`1024. 视频拼接` https://leetcode-cn.com/problems/video-stitching/solution/shi-pin-pin-jie-by-leetcode-solution/
- [x] 方法一：动态规划
- [x] 方法二：贪心

# 测试用例

```
[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
10
[[0,1],[1,2]]
5
[[0,1],[2,5]]
5
[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
9
```

# 语法点

```py
infinite = float("inf")
print infinite
print infinite + 1
print float("inf") / 2
print 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 > float("inf")

print float("-inf")
print -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 < float("-inf")

import sys
print sys.maxint
print sys.maxint > float("inf")
----------------------------------------------------------------------------------------------------
inf
inf
inf
False
-inf
False
9223372036854775807
False
```
