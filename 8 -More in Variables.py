#                       "Multi Variables" but Same Value

# If one variable value is same to another one or more variables, Their address will be same.

# 'Garbage Collection' means one value stored in memory address that value is not used to another variables.
'''
num = 3
print('num :', id(num)) #o/p: 2503672424816

name = "raja"
print('name :', id(name)) #o/p: 2021255173168

a = 20
b = a 
print("a :", id(a)) #o/p: 2278299036560

print("b :", id(b)) #o/p: 2278299036560

print("value 20 :",id(20)) #o/p: 2278299036560

c = 20
print("c :", id(c)) #o/p: 2278299036560

a = 21
print("a :", id(a)) #o/p: 2631851338672

print("b :", id(b)) #o/p: 2278299036560 still refering previous assignment address of value

c = a
print("c :", id(c)) #o/p: 2631851338672
'''
#                       type() function

# Python have no 'const' Constant Function.
# Constant reffer in capital letters Variable.
# we ca show the intension of Constant by using Capital Variables.
PI = 3.14
print(type(PI)) #o/p: <class 'float'>
















