__author__ = 'Administrator'


class Student(object):
    pass


st = Student()
st.name = "hello"  # 给实例绑定属性
print(st.name)


def set_age(self, age):
    self.age = age


from types import MethodType

st.set_age = MethodType(set_age, st) # 给st绑定一个函数
st.set_age(10)
print(st.age)
