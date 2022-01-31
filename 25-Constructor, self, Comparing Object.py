#         Address of Object
# Multiple objects memory address will be different

# class Company:
#     pass
#
# company1 = Company()
# company2 = Company()
#
# print(id(company1))
# print(id(company2))
'''o/p:
2864838798208
2864838798448
'''

#        Constructor __init__ & Changing values

# class Company:
#     def __init__(self):
#         self.name = 'Ragu'
#         self.age = 20
#
# company1 = Company()
#
# print(company1.name)
# print(company1.age)
#
# company2 = Company()
# company2.name='sam'  # Changing values
# company2.age=21
#
# print(company2.name)
# print(company2.age)
'''o/p:
Ragu
20
sam
21
'''

#      Updating or change values

# class Company:
#     def __init__(self):
#         self.name = 'Ragu'
#         self.age = 20
#
#     def update(self): # (Which Object is calling is self)
#         self.name = "Ravi"
#         self.age = 21
#
# company1 = Company()
# company2 = Company()
#
# company2.update()
#
# print(company1.name)
# print(company1.age)
#
# print(company2.name)
# print(company2.age)
'''o/p:
Ragu
20
Ravi
21
'''

#      Comparing Two Objects

class Company:
    def __init__(self):
        self.name = 'Ragu'
        self.age = 20
    #(who is calling, whome to compare)
    def compare(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

company1 = Company()
company2 = Company()
company2.name='sam'
company2.age=21

if company1.compare(company2): # Comparing
    print('Same name and age')
else:
    print('Different name and age')

print(company1.name)
print(company1.age)

print(company2.name)
print(company2.age)
'''o/p:
Different name and age
Ragu
20
sam
21
'''






