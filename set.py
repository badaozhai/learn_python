__author__ = 'Administrator'
l = [1, 2, 3, 4, 5, 5, 5, 2, 3, 4]
s = set(l)
print(s)
# 添加一个元素
s.add(9)
print(s)
# 添加元素,如果已经存在,但是不起作用
s.add(5)
print(s)
# 删除元素
s.remove(5)
print(s)