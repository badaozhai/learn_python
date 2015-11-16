__author__ = 'Administrator'
names = ['zhangfei', 'liubei', 'guanyu']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

li = list(range(100))
print(li)

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 1
while n < 101:
    sum = sum + n
    n = n + 1
print(sum)

L = ['bart', 'lisa', 'adam']
for x in L:
    print('hello,', x, '!')
