class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        """
        已发现错误：
        "12345678" * "12345678" = "152415765279684" 是对的，但是：
        "123456789" * "123456789" = "15241577750190521"，正确值应为："15241578750190521"
        纵向对比下看看，就一位不一样（后面再各加一个9，错位也不多，所以可能哪有小错误），打算先提交下。
        "15241577750190521"
        "15241578750190521"
        """

        def string_multiply_with_single(s, ch):
            carryflag, res = 0, ''
            for i in range(len(s)-1,-1,-1):
                tmp = int(s[i]) * int(ch) + carryflag
                res = str(tmp % 10) + res
                carryflag = tmp / 10
            return res
        
        # 这里几乎就是把`000415.py`的内容绝大部分复制过来了。。。
        def string_add(num1, num2):
            flag, res = 0, ''
            len1, len2 = len(num1), len(num2)
            if len1 >= len2:
                longer, shorter, lenlonger, lenshorter = num1, num2, len1, len2
            else:
                longer, shorter, lenlonger, lenshorter = num2, num1, len2, len1
            for i in range(-1,-lenshorter-1,-1):
                summation = int(longer[i]) + int(shorter[i]) + flag
                if summation >= 10:
                    res = str(summation % 10) + res
                    flag = 1
                else:
                    res = str(summation) + res
                    flag = 0
            for j in range(-lenshorter-1,-lenlonger-1,-1):
                summation = int(longer[j]) + flag
                if summation >= 10:
                    res = str(summation % 10) + res
                    flag = 1
                else:
                    res = str(summation) + res
                    flag = 0
            if flag == 1:
                res = '1' + res
            return res

        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        len1, len2 = len(num1), len(num2)
        if len1 >= len2:
            longer, shorter, lenlonger, lenshorter = num1, num2, len1, len2
        else:
            longer, shorter, lenlonger, lenshorter = num2, num1, len2, len1
        
        for i in range(lenshorter-1,-1,-1):
            tmpres = string_multiply_with_single(longer, shorter[i])
            # 乘完还要在末尾加一定数量的0
            for j in range(lenshorter-1-i):
                tmpres = tmpres + '0'
            res = string_add(res, tmpres)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/97676273/

33 / 311 个通过测试用例
状态：解答错误

输入：
"9"
"9"
输出：
"1"
预期：
"81"
"""
