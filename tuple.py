__author__ = 'Administrator'
l = ['a', 'b']
classmates = ('张飞', '刘备', '关羽', l)

print(classmates)

print(len(classmates))

print(classmates[0])

# print(classmates[3])  # 和list一样 越界会报错

# classmates[0] = 'hello' # tuple是不可变的
# print(classmates)

classmates[3][0] = 'x'
print(classmates)
