__author__ = 'Administrator'
t = type(123)
print(t)  # int

print(t)  # str


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()

print(len(dog))
