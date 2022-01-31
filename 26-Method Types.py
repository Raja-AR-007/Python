#                    Types of Methods
# Instance Method (Accessors,Mutators)
# Class Method
# Static Method

#              Instance Method
'''
class Student:

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # Instance Method
        return (self.m1+self.m2+self.m3)/3

s1 = Student(34, 23, 45)
s2 = Student(67, 43, 56)

print("student1 avg:",s1.avg())
print("student2 avg:",s2.avg())
'''
'''o/p:
student1 avg: 34.0
student2 avg: 55.333333333333336
'''

#        Accessor, Mutator Methods
# 'Accessor' will access the value.
# 'Mutators' will change the value.
'''
class Student:

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # Instance Method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):  # Accessor Method
        return self.m1

    def set_m1(self,value): # Mutator Method
        self.m1 = value

s1 = Student(34, 23, 45)
s2 = Student(67, 43, 56)

print('student m1:',s1.get_m1()) # calling Accessor
s1.set_m1(99) # calling Mutator to change the value
print('student changed m1:',s1.m1)
'''
'''o/p:
student m1: 34
student changed m1: 99
'''

#                @classmethod
# 'cls' Should only use in the parameter
'''
class Student:
    school= "Navarasam"
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def schlMethod(cls): # 'cls' Should only use
        return cls.school

s1 = Student(34, 23, 45)
s2 = Student(67, 43, 56)

print('School :',Student.schlMethod()) # calling class method
'''
'''o/p:
School : Navarasam
'''

#            @staticmethod
# By using @staticmethod we can operate another class objects.
# or we can do anything.

class Student:
    school= "Navarasam" # for all Objects
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @staticmethod
    def info():  # Static Method
        print("We can use @staticmethod for any process")

s1 = Student(34, 23, 45)
s2 = Student(67, 43, 56)

s1.info() # calling Static method

'''o/p:
We can use @staticmethod for any process
'''