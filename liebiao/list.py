__author__ = 'Administrator'
classmates = ['zhangfei','lilei','liubei']
print(classmates)
print(len(classmates))
print(classmates[0])
# print(classmates[3]) #超过界限会报错

print(classmates[-1])   # 倒数第一个

print(classmates[-2])   # 倒数第二个

classmates.append('lvbu') #尾部追加一个元素
print(classmates)
print(len(classmates))


classmates.pop(2)    # 删除一个 默认是最后一个
print(classmates)
print(len(classmates))


classmates[0] = 'hello' #替换某个元素
print(classmates)
print(len(classmates))


L = ['apple',11,True]
print(L)


s = ['python','java',L]
print(len(s))
print(s)


x = []
print(len(x))

