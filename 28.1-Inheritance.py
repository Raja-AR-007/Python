#             Single level inheritance
'''
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

a1 = A()

b1 = B()
b2 = B()

b1.feature1()
b2.feature2()
'''
'''o/p:
This is feature 1
This is feature 2
'''
#           Multi level inheritance
'''
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C(B):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

a1 = A()

b1 = B()

c1 = C()
c2 = C()

c1.feature1()
c2.feature3()
'''
'''o/p:
This is feature 1
This is feature 3
'''

#             Multiple inheritance

class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B:
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C (A, B):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")
a1 = A()

b1 = B()

c1 = C()
c2 = C()

c1.feature1()
c1.feature3()
'''o/p:
This is feature 1
This is feature 3
'''