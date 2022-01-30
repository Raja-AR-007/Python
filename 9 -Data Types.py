#                              Data Types
'''
None
Numeric (int, float, complex, bool)
List
Tuple
Set
String
Range
Dictionary or Mapping
'''

#                          None

# value is not assigned to variable
# will define it as None but in other lang is Null
 
#                          Numeric (int, float, complex, bool)

#                     int

num = 3
print(type(num)) 
#o/p: <class 'int'>

#                     float

num = 4.6
print(type(num)) 
#o/p: <class 'float'>

#                     complex

num = 4+6j #j means 'root of -1'
print(type(num)) 
#o/p: <class 'complex'>

#                      bool

num = 5<6
print(num) 
# o/p: True
print(type(num)) 
#o/p: <class 'bool'>

k = 6>9
print(k) 
# o/p: False

#                    Numeric Convertions
#           float to int
a = 2.9
b = int(a)
print(b) 
#o/p: 2

#           int to float
k = float(b)
print(k) 
#o/p: 2.0

#            to complex
c = complex(b, k)
print(c) 
#o/p: (2+2j)

#           bool to int
m = int(True)
print(m) 
#o/p: 1

n = int(False)
print(n) 
#o/p: 0


#       Sequence data types

#List, Tuple, Set, String, Range

#                      List[] -> mutable

lst = [1, '3', "raja", 'MCA']
print(type(lst))
#o/p: <class 'list'>

#                      Tuple() -> immutable

tup = (1, '3', "raja", 'MCA')
print(type(tup))
#o/p: <class 'tuple'>

#                      Set{} -> output is non-sequence
# Set will not repeat the duplicate values

s = {1, '3', "raja", 'MCA'}
print(type(s))
#o/p: <class 'set'>

#                     String
str = "raja"
print(type(str))
#o/p: <class 'str'>

# There is no specific char data type in python.
# String can also handle the char data type.
st = 'r'
print(type(st))
#o/p: <class 'str'>

#                     range()

r = range(5)
print(r)
#o/p: range(0, 5)

# by convert range into list we can see all numbers
r1 = list(r)
print(r1)
#o/p: [0, 1, 2, 3, 4]

r2 = list(range(2, 9))
print(r2)
#o/p: [2, 3, 4, 5, 6, 7, 8]

r3 = list(range(3, 10, 3))
print(r3)
#o/p: [3, 6, 9]

#                         Dictionary or mapping
# Mapping format {key:value}
d = {'raja':'oppo', 'gowtham':'onu plus', 'harish':'asus', 'mohan':"mi"} 
print(type(d)) #o/p: <class 'dict'>

print(d.keys()) 
#o/p: dict_keys(['raja', 'gowtham', 'harish', 'mohan'])

print(d.values()) 
#o/p: dict_values(['oppo', 'onu plus', 'asus', 'mi'])

print(d["mohan"]) # square bracket[key]
#o/p: mi

print(d.get("gowtham")) # get(key)
#o/p: onu plus