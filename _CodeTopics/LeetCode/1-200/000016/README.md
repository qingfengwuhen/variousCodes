
https://leetcode-cn.com/problems/3sum-closest/solution/
>> //note：看了看基本就是暴力三重循环和双指针两种办法，没有别的算法了。我双指针的最后一个实现（`000016_algo2_optm.py`）感觉已经优化到头了，为什么还只是比20%多的人快，目前没想出来啥原因。。。
>>> 后来对比了一下`LC15`当时的代码，明白了。原来是最小的位置 i 也可能有很多重复值，也可以跳过。后面的`000016_algo2_optm2.py`超过70%多的提交还算说得过去。
