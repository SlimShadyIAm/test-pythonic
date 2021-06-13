from collections import namedtuple

Person = namedtuple('Person', 'name age')
p1 = Person("Aamir", 21)
p1 
Person(name='Aamir', age=21)