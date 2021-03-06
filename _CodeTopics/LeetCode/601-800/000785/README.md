
`785. 判断二分图` https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/
- 方法一：深度优先搜索
- 方法二：广度优先搜索

# `TLE--000785_algo2.py`

这个本来是用子函数的，原来的代码是这样的：
```py
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        length = len(graph)
        s1, s2 = set([0]), set(graph[0])
        leftIndexes = []

        def processElemI(i):
            tempset = set(graph[i])
            if i in s1 and i in s2:
                return False
            elif i in s1:
                s2 = s2.union(tempset)
            elif i in s2:
                s1 = s1.union(tempset)
            else:
                if s1.intersection(tempset) and s2.intersection(tempset):
                    return False
                elif s1.intersection(tempset):
                    s1 = s1.union(tempset)
                    s2.add(i)
                elif s2.intersection(tempset):
                    s2 = s2.union(tempset)
                    s1.add(i)
                else:
                    leftIndexes.append(i)
            if s1 & s2:
                return False

        for i in range(1,length):
            if not processElemI(i):
                return False
        while leftIndexes:
            index = leftIndexes.pop(0)
            if not processElemI(index):
                return False
        return True
```

但是不知道为什么用子函数的话总是提示这个错：
```
Exception has occurred: UnboundLocalError local variable 's1' referenced before assignment
```
- 问题在于，我并查集那个题（ https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000990/000990_algo2_2.py ）也用到了一个变量`fa`啊，为啥那个代码里没报错。回来再看了。。。
- 奇怪的是，我后来自己又用并查集实现了一下这个题，里面也有`fa`，并且也和这里的`s1或s2`地位类似啊，但是AC了，并且也没有`referenced before assignment`的问题啊。
