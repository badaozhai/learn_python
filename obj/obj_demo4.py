__author__ = 'Administrator'


class Student(object):
    def __init__(self, name, sex):
        self.__name = name
        self.__sex = sex

    def print_self(self):
        print('print_self:', self.__name, self.__sex)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


bart = Student('zhangfei', '男')
# bart.__name = '123'
# print(bart.__name) # 私有属性不可访问
print(bart.get_name())
bart.set_name('guanyu')
print(bart.get_name())
bart.print_self()
