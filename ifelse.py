__author__ = 'Administrator'

age = 4
if age > 3:
    print('age > 3')
else:
    print('age<=3')

age = 15
if age < 10:
    print('小孩')
elif age > 10 and age < 30:
    print('中年')
else:
    print('老年')

#
# age = input()
# age = int(age)      # 需要进行类型转化 字符串和数字是不可以比较的
# if age<10:
#     print('小孩')
# else:
#     print('大孩子')


shengao = input('输入身高(米):')
tizhong = input('输入体重(kg):')
res = float(tizhong) / (float(shengao) * float(shengao))

if res < 18.5:
    print('过轻')
elif res >= 18.5 and res < 25:
    print('正常')
elif res >= 25 and res < 28:
    print('过重')
elif res >= 28 and res < 32:
    print('肥胖')
elif res >= 32:
    print('严重肥胖')
