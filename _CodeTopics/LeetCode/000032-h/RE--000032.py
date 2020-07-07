class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        思路：动态规划。主要的难点就是递推公式略有些绕，相通了也就还好。
        """

        if not s:
            return 0
        
        length = len(s)
        dp = [0] * length
        dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0
        
        for i in range(2,length):
            if s[i] == '(':
                dp[i] = 0
            else:   # 此时 s[i] 等于 ')'
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:   # 此时 s[i-1] 等于 ')'，也就是这个题里最复杂的部分
                    if s[i-dp[i-1]-1] == '(':
                        dp[i] = (dp[i-1] + 2) + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/85705543/

3 / 230 个通过测试用例
状态：执行出错

执行出错信息：Line 17: IndexError: string index out of range
最后执行的输入："("
"""
