class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # 用内置的map()加lambda来代替列表推导式。
        subtraction = map(lambda x, y : x-y, gas, cost)
        if sum(subtraction) < 0:
            return -1

        length = len(subtraction)
        for i in range(length):
            addition = subtraction[i]
            j = i + 1
            while addition >= 0 and j % length != i:
                addition += subtraction[j%length]
                j += 1
            if addition < 0:
                continue
            if j % length == i:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/124243093/

31 / 31 个通过测试用例
状态：通过
执行用时: 2144 ms
内存消耗: 14.2 MB

执行用时：2144 ms, 在所有 Python 提交中击败了25.40%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了7.67%的用户
"""
