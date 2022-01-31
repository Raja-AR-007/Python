#                Inner class

# Creating object of inner class in inside of the outer class,
# printing inner class value.
'''
class Student: # outer class
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap1 = self.Laptop() # Object of inner class here can create

    def show(self):
        print(self.name, self.rollNo)

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4Gb'

s1 = Student('Ragav', 3)
s2 = Student("fathi", 4)

s1.show()

print(s1.lap.brand) # inner class value
'''
'''o/p:
Ragav 3
Lenovo    # inner class
'''

# checking memory address of inner class object
# and which is created outside of outer class.
'''
class Student: # outer class
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap1 = self.Laptop() # Object of inner class here can create

    def show(self):
        print(self.name, self.rollNo)

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4Gb'

s1 = Student('Ragav', 3)
s2 = Student("fathi", 4)

s1.show()

lap2 = s1.lap1 # Another way to create inner class Object
lap3 = s2.lap1
print('Address \n',id(lap2),'\n',id(lap2))
'''
'''o/p:
Ragav 3
Address 
 2676676329328 
 2676676329328
'''

# Creating inner class Object in proper way

# we can create object of inner class in outside of the outer class,
# and provided we can use outer class name to call inner class.

class Student: # outer class
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap1 = self.Laptop() # Object of inner class here can create

    def show(self):
        print(self.name, self.rollNo)

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4Gb'

s1 = Student('Ragav', 3)
s2 = Student("fathi", 4)

s1.show()


# Creating object of inner class in inside and outside of the outer class,
# and calling inner class method inside of outer class method.
'''
class Student: # outer class
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap1 = self.Laptop() # object of inner class

    def show(self):
        print(self.name, self.rollNo)
        self.lap1.show() # calling inner class Method 

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4Gb'

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Ragav', 3)
s2 = Student("fathi", 4)
s1.show()
s2.show()
'''
'''o/p:
Ragav 3        # outer class
Lenovo i5 4Gb   # inner class
fathi 4
Lenovo i5 4Gb
'''

# Creating object of inner class in outside of the outer class,
'''
class Student: # outer class
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def show(self):
        print(self.name, self.rollNo)

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '4Gb'

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Ragav', 3)
s2 = Student("fathi", 4)
s1.show()
s2.show()

lap1 = Student.Laptop()
lap2 = Student.Laptop()
lap1.show()
lap2.show()
'''
'''o/p:
Ragav 3
fathi 4
Lenovo i5 4Gb
Lenovo i5 4Gb
'''