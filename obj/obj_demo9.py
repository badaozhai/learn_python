__author__ = 'Administrator'
class Student(object):
    @property
    def scorehello(self):
        return self._score
    @scorehello.setter
    def scorehello(self,value):
        if not isinstance(value,int):
            raise ValueError("分数必须是个整数")
        if value<0 or value>100:
            raise ValueError("数字太大了")
        self._score = value

st = Student()
st.scorehello = 60
st.scorehello = 999
print(st.scorehello)