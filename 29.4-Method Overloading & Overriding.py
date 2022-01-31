'''
class Add:
    def operation(self, a,b,c):
        d = a + b+ c
        return d

add1 = Add()

z = add1.operation(1,2,4)
print(z) # o/p: 7
'''

#         python don't have Method Overloading

# we can achieve that Method Overloading in another way Trick.

class Add:
    def operation(self, a=None,b=None,c=None):
        d = 0
        if a!=None and b!=None and c!=None:
            d = a + b+ c
        elif a!=None and b!=None:
            d = a + b
        elif a != None:
            d = a
        return d

add1 = Add()

z = add1.operation(12, 25)
print("Addition of Two Arguments:",z)
print("Addition of One Argument:",add1.operation(44))
print("Addition of Three Arguments:",add1.operation(12, 45, 78))

'''o/p:
Addition of Two Arguments: 37
Addition of One Argument: 44
Addition of Three Arguments: 135
'''

#             Inheritance
'''
class A:
    def show(self):
        print("It is show() A")
        
class B(A):
    pass

a1 = A()

b1 = B()
b1.show()
'''
'''o/p:
It is show() A
'''

#                Method Overriding

class A:
    def show(self):
        print("It is show() A")

class B(A):
    def show(self):
        print("It is show() B")

a1 = A()

b1 = B()
b1.show()

'''o/p:
It is show() B
'''