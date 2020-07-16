

```py
dp1 = [[0 for i in range(4)] for j in range(3)]
print "dp1 = ", dp1
dp2 = [[0] * 4 for j in range(3)]
print "dp2 = ", dp2
print dp1 == dp2

dp3 = [[0] * i for i in range(4) for j in range(3)]
print "dp3 = ", dp3
dp4 = [[[0] * i for i in range(4)] for j in range(3)]
print "dp4 = ", dp4

dp5 = [[0] * i for i in range(1,4)]
print "dp5 = ", dp5
----------------------------------------------------------------------------------------------------
dp1 =  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
dp2 =  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
True
dp3 =  [[], [], [], [0], [0], [0], [0, 0], [0, 0], [0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
dp4 =  [[[], [0], [0, 0], [0, 0, 0]], [[], [0], [0, 0], [0, 0, 0]], [[], [0], [0, 0], [0, 0, 0]]]
dp5 =  [[0], [0, 0], [0, 0, 0]]
```