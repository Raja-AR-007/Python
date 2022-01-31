#                   Constructor in Inheritance

# If create Object of subclass then it will first try to find __init__ of subclass
# and if it is not found then it will call __init__ of superclass

# Constructor '__init__' not Created in subclass
'''
class A:
    def __init__(self):
        print('Constructor __init__ A')
    def feature1(self):
        print('This is feature 1-A')
    def feature2(self):
        print('This is feature 2-A')
class B(A):
    def feature1(self):
        print('This is feature 1-B')
    def feature4(self):
        print('This is feature 4-B')

a1 = A()
a1.feature1()

b1= B()
b1.feature1()
'''
'''o/p:
Constructor __init__ A
This is feature 1-A
Constructor __init__ A  # see here
This is feature 1-B
'''

# Constructor '__init__' created in subclass
'''
class A:
    def __init__(self):
        print('Constructor __init__ A')
    def feature1(self):
        print('This is feature 1-A')
    def feature2(self):
        print('This is feature 2-A')
class B(A):
    def __init__(self):  # see here
        print('Constructor __init__ B')
    def feature1(self):
        print('This is feature 1-B')
    def feature4(self):
        print('This is feature 4-B')

a1 = A()
a1.feature1()

b1= B()
b1.feature1()
'''
'''o/p:
Constructor __init__ A
This is feature 1-A
Constructor __init__ B  # see here
This is feature 1-B
'''

#                Super

# when you create object of Subclass it will call __init__ of Subclass first,
# In subclass if you call Super then it will first call __init__ of superclass
# and then second it will call __init__ of Subclass.

#      Super Constructor call, Super Method call

# In Multi level inheritance Super is used to access superclass features
'''
class A:
    def __init__(self):
        print('Constructor __init__ A')
    def feature1(self):
        print('This is feature 1-A')
    def feature2(self):
        print('This is feature 2-A')
class B(A):
    def __init__(self):
        super().__init__()  # Super Constructor call
        print('Constructor __init__ B')
    def feature1(self):
        super().feature1()  # Super Method call
        print('This is feature 1-B')
    def feature4(self):
        print('This is feature 4-B')
b1= B()
b1.feature1()
'''
'''o/p:
Constructor __init__ A
Constructor __init__ B
This is feature 1-A
This is feature 1-B
'''

#             Method Resolution Order 'MRO'

# If we use Super Constructor, Super Method in
# Multiple Inheritance C(A,B) 'it will take only Left to Right'
# depends on position in parameter and in this case is A class is in Left

class A:
    def __init__(self):
        print('Constructor __init__ A')
    def feature1(self):
        print('This is feature 1-A')
    def feature2(self):
        print('This is feature 2-A')

class B:
    def __init__(self):
        print('Constructor __init__ B')
    def feature1(self):
        print('This is feature 1-B')
    def feature4(self):
        print('This is feature 4-B')

class C(A, B):  #
    def __init__(self):
        super().__init__()  # Super Constructor call
        print('Constructor __init__ C')
c1 = C()
c1.feature1()

'''o/p:
Constructor __init__ A
Constructor __init__ C
This is feature 1-A
'''

'''
class A:
    def __init__(self):
        print('Constructor __init__ A')
    def feature1(self):
        print('This is feature 1-A')
    def feature2(self):
        print('This is feature 2-A')

class B:
    def __init__(self):
        print('Constructor __init__ B')
    def feature1(self):
        print('This is feature 1-B')
    def feature4(self):
        print('This is feature 4-B')

class C(A, B):  #
    def __init__(self):
        super().__init__()  # Super Constructor call
        print('Constructor __init__ C')
    def feat(self):
        super().feature4()  # Super Method call
c1 = C()
c1.feat()
'''
'''o/p:
Constructor __init__ A
Constructor __init__ C
This is feature 4-B
'''