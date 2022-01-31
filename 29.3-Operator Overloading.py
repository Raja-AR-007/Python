
# Built-in function
'''
x = 8
y = 7

# Automatically it calling __add__() Method
print(x + y) #15

# Manually calling __add__() Method
print(int.__add__(x,y))  # 15
'''

#                       Operator Overloading

# It is Overloading built-in Operator Methods
# for example __add__(), __mul__(), __sub__(), __gt__() Methods
# or user defining the built-in Method for own purpose.
'''
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

s1 = Student(23, 45)
s2 = Student(56, 43)

s3 = s1 + s2
'''
'''o/p:
    s3 = s1 + s2
TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
'''

#  Overloading __add__() built-in Operator Method

# adding s1 and s2 and 'assigning' sum value to s3 Object 's3=s1+s2'
'''
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
        
s1 = Student(23, 45)
s2 = Student(56, 43)

s3 = s1 + s2  # -> Student.__add__(s1,s2)

print("Addition of s1.m1 + s2.m1 =",s3.m1)
print("Addition of s1.m2 + s2.m2 =",s3.m2)
'''
'''o/p:
Addition of s1.m1 + s2.m1 = 79
Addition of s1.m2 + s2.m2 = 88
'''

#  Overloading __add__() built-in Operator Method

# adding s1 and s2 and 'not assigning' sum value to s3 Object
'''
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return m1, m2


s1 = Student(23, 45)
s2 = Student(56, 43)
# first way to print
print("Addition of s1 and s2 marks:",Student.__add__(s1,s2))
# second way to print
print("Addition of s1 and s2 marks:",s1.__add__(s2))
'''
'''o/p:
Addition of s1 and s2 marks: (79, 88)
Addition of s1 and s2 marks: (79, 88)
'''
#  Overloading __gt__() built-in Operator Method
'''
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):  # Operator overloading
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = Student(55, 45)
s2 = Student(56, 43)

if s1 > s2:
    print("s1 is greater s2")
else:
    print("s2 is greater s1")
'''
'''o/p:
s1 is greater s2
'''

#  Overloading __str__() built-in Operator Method
'''
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):  # Operator Overloading
        return self.m1, self.m2

s1 = Student(55, 45)
s2 = Student(56, 43)

# printing value not address
a = 2
print(a.__str__())  # calling built-in Method

print(s1.__str__())  # calling defined Method
'''
'''o/p:
2
(55, 45)
'''

#  Overloading __add__() built-in Operator Method
#  Overloading __gt__() built-in Operator Method
#  Overloading __str__() built-in Operator Method

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):  # Operator overloading
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):  # Operator Overloading
        return self.m1, self.m2

s1 = Student(55, 45)
s2 = Student(56, 43)

s3 = s1 + s2
print("Addition of s1.m1 + s2.m1 =",s3.m1)

if s1 > s2:
    print("s1 is greater s2")
else:
    print("s2 is greater s1")

# printing value not address
a = 2
print(a.__str__())
# o/p: 2

print(s1.__str__())
# o/p: (55, 45)

'''o/p:
Addition of s1.m1 + s2.m1 = 111
s1 is greater s2
2
(55, 45)
'''

# Overloading __add__ built-in Operator Method
# Addition of s1 marks m1, m2.
'''
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self):  # Operator overloading
        self = self.m1 + self.m2
        return self


s1 = Student(23, 45)
s2 = Student(56, 43)
print("Addition of s1 marks:",Student.__add__(s1))
print("Addition of s1 marks:",s1.__add__())
'''
'''o/p:
Addition of s1 marks: 68
Addition of s1 marks: 68
'''