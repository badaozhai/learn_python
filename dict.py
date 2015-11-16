__author__ = 'Administrator'

d = {'mm': 11, 'xx': 22, 'yy': 33}
print(d['mm'])
d['mm'] = 999
d['mm'] = 88
print(d)

# print(d['aa'])  # 如果key不存在就报错

# 判断一个key是否在dict中
isin = 'aa' in d
print(isin)

isin2 = d.get('aa')
print(isin2)

