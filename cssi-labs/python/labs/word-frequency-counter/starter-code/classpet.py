class Pet:
    '''__init__() is a method of the class pet
    .A method is a function that belongs to a
    class instance. All methods of a class first
    parameter is self'''
    def __init__(self,name,age,animal="Dog"):
        '''self.name and self.age are intance attribute or
        data members of the class Pet. instance attributes
        are unique in every accurrance (instance) of a Pet object'''
        self.name = name
        slef.age = age
        self.animal = animal
        self.is_hunger = False
        self.mood = "happy"

    def eat(self):
        self.is_hunger = False

    def __str__(self):
        return 

    count = 0
'''The Pet class has the members age,name,count, __init()__selfself.
To call the __init__() function we use the class name with the
resoective parameters within parenthesis'''

def madeHunger(pet):
    pet.is_hunger = True

#o is an object of pet
o = Pet("Dog", 3)

#t is another object of property
t = Pet("Cat",4)

print "Before call to madeHunger()"
print o.name, o.age, o.is_hunger
print t.name, t.age, t.is_hunger


madeHunger(o)

print "After call to madeHunger() and before call to eat()"
print o.name, o.age, o.is_hunger
print t.name, t.age, t.is_hunger

o.eat()

print "After call to eat()"
print o.name, o.age, o.is_hunger
print t.name, t.age, t.is_hunger

print o
