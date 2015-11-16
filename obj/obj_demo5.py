__author__ = 'Administrator'


class Animal(object):
    def run(self):
        print('ruing')


# 继承了Animal
class Dog(Animal):
    def run(self):
        print('dog is ruing')

    def eat(self):
        print('dog is eating')


class Cat(Animal):
    def run(self):
        print('cat is running')

    pass


dog = Dog()
dog.eat()
cat = Cat()
cat.run()
