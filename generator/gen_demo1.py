__author__ = 'Administrator'
for x in range(1, 10):
    print(x)
l = list(range(10))
print(l)
# 列表生成式
li = [x * x for x in range(10)]
print(li)
li = [x * x for x in range(10) if x%2==0]
print(li)
lis = [m + n for m in 'ABC' for n in 'XYZ']
print(lis)

import os
l=[d for d in os.listdir('.')]
print(l)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)
# 生成器
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = (x for x in L1 if isinstance(x, str))
print(L2)
for n in L2:
    print(n)