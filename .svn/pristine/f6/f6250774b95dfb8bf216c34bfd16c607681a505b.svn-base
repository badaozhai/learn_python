__author__ = 'Administrator'


class Student(object):
    # __slots__ 只能对当前的起作用不能对之类起作用
    __slots__ = ('name', 'age')


st = Student()
st.name = '123'
print(st.name)
st.age = 11
print(st.age)


# st.score = 33
# print(st.score)

class GaStudent(Student):
    pass


ga = GaStudent()
ga.score = 111
print(ga.score)
