__author__ = 'Administrator'

#定义student类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, self.score)


bart = Student('bart', 59)
bart.print_score()
