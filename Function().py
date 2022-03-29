#               Function()
'''
def student():
    print("Welcome to python")

student()
'''
'''o/p:
Welcome to python
'''


#     parameter & Argument
'''
def student(name, rollNo, cls, m1, m2, m3, m4, m5): # Parameter
    print("Name    :", name)
    print("Roll No :", rollNo)
    print("Class   :", cls)
    print("Mark1   :", m1)
    print("Mark2   :", m2)
    print("Mark3   :", m3)
    print("Mark4   :", m4)
    print("Mark5   :", m5)

student("Raja", "20ca020", "I-MCA", 95, 94, 93, 92, 96) #Argument
'''
'''o/p:
Name    : Raja
Roll No : 20ca020
Class   : I-MCA
Mark1   : 95
Mark2   : 94
Mark3   : 93
Mark4   : 92
Mark5   : 96
'''

#       Argument with Key

def student(name, rollNo, cls, m1, m2, m3, m4, m5): # Parameter
    print("Name    :", name)
    print("Roll No :", rollNo)
    print("Class   :", cls)
    print("Mark1   :", m1)
    print("Mark2   :", m2)
    print("Mark3   :", m3)
    print("Mark4   :", m4)
    print("Mark5   :", m5)

student(name="Raja", rollNo="20ca020", cls="I-MCA", m1=95, m2=94, m3=93, m4=92, m5=96) #Argument with key

'''o/p:
Name    : Raja
Roll No : 20ca020
Class   : I-MCA
Mark1   : 95
Mark2   : 94
Mark3   : 93
Mark4   : 92
Mark5   : 96
'''

#    Defalut argument values in parameter
'''
def student(name="Raja", rollNo="20ca020", cls="I-MCA", m1=95, m2=94, m3=93, m4=92, m5=96): # Default values
    print("Name    :", name)
    print("Roll No :", rollNo)
    print("Class   :", cls)
    print("Mark1   :", m1)
    print("Mark2   :", m2)
    print("Mark3   :", m3)
    print("Mark4   :", m4)
    print("Mark5   :", m5)

student()
'''
'''o/p:
Name    : Raja
Roll No : 20ca020
Class   : I-MCA
Mark1   : 95
Mark2   : 94
Mark3   : 93
Mark4   : 92
Mark5   : 96
'''

#                    * operator in function parameter
'''
def student(*val): # Parameter
    print("Student details:", val)

student("Raja", "20ca020", "I-MCA", 95, 94, 93, 92, 96) #Argument
'''
'''o/p:
Student details: ('Raja', '20ca020', 'I-MCA', 95, 94, 93, 92, 96)
'''