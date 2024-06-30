# aaja ko kilaas ma hami class ko barema sikxaum
# create a class
class myClass:
    myVar = 5
    
# define object for class
meroObj1 = myClass()
print(meroObj1.myVar)

# let's get started
class Person:
    species = 'homo sapiens'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printName(self):
        print(f'My name is {self.name}')
        
    def printAge(self):
        print(f'My age is {self.age}')
    
p1 = Person('Binod', 32)
p1.printAge()
p1.printName()
print(p1.species)
p1.species = 'khai k ho k ho'

p2 = Person('Sudeep',22)
p2.printAge()
print(p2.species)

# Inheritance 
# Let's create a child class for Class Person
class student(Person):
    def __init__(self, name, age, crn):
        super().__init__(name, age)
        self.crn = crn
        
    def printCRN(self):
        print(f'my crn is {self.crn}')

s1 = student('PuriG', 21, 420)
s1.printName()
s1.printAge()
s1.printCRN()

# Encapsulation
s1.age = 40
print(s1.printAge())
# This changes the values and we might not want this
# so we need to do encapsulation

class car:
    def __init__(self, topspeed):
        self.__topspeed = topspeed
        
    def printTopSpeed(self):
        print(f'The top speed is {self.__topspeed}')
        
    def setTopSpeed(self, newSpeed):
        self.__topspeed = newSpeed
    
    def getTopSpeed(self):
        return self.__topspeed
    
        
nanoCar = car(100)
nanoCar.printTopSpeed()
nanoCar.topspeed = 20000
nanoCar.printTopSpeed()
nanoCar.setTopSpeed(80)
nanoCar.printTopSpeed()
print(nanoCar.getTopSpeed())
# print(nanoCar.__topspeed) # can't access private 

# Polymorphism
class bird:
    def __init__(self, name):
        self.name = name
        
    def fly(self):
        print(f'{self.name} can fly')

class penguin(bird):
    def fly(self):
        print(f'{self.name} can not fly')

class sparrow(bird):
    pass

peng1 = penguin('Pengu')
peng1.fly()

bird1 = sparrow('spaww')
bird1.fly()
