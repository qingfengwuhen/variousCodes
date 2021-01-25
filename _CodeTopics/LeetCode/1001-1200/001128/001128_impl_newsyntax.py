class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        dic = {}
        for x, y in dominoes:
            x, y = min(x,y), max(x,y)
            currKey = tuple([x,y])
            """
            if not dic.has_key(currKey):
                dic[currKey] = 1
            else:
                dic[currKey] += 1
            """
            # 上面这段代码准备用字典自带的方法 setdefault() 来写。
            dic.setdefault(currKey, 0)
            dic[currKey] += 1
        
        res = 0
        for v in dic.values():
            if v >= 2:
                res += v * (v-1) / 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/141164731/

19 / 19 个通过测试用例
状态：通过
执行用时: 204 ms
内存消耗: 24.7 MB

执行用时：204 ms, 在所有 Python 提交中击败了78.87%的用户
内存消耗：24.7 MB, 在所有 Python 提交中击败了38.03%的用户
"""
