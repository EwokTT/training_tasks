class Person:
    def __init__(self,name):
        self.name=name
        self.age=20
    def print_info(self):
        print (f'Hello, my name is {self.name} Age: {self.age}')

person1=Person('Jhin')
person1.age=30
person1.print_info()
