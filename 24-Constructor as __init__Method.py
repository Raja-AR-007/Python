#                        __init__ Method also called as Constructor
'''
class School:
    def __init__(self, name, rollNo):
        self.name1 = name
        self.rollNo1 = rollNo

    def studDetails(self):  # This Method is structure to store values
        print("Details :", "\nStud name:",self.name1, "\nstud RollNo:",self.rollNo1)

stud1 = School("Raja", "21CA020")

stud1.studDetails()
'''
'''o/P:
Details :
Stud name: Raja
stud RollNo: 21CA020
'''

#   Local variable can be same or different to parameterized variables

class School:
    def __init__(self, name, rollNo):
        self.name = name  # Local variable can be same or different
        self.rollNo = rollNo

    def studDetails(self):  # This Method is structure to store values
        # 'self.name,self.rollNo' means Method & Variable working together
        print("Details :", "\nStud name:",self.name, "\nstud RollNo:",self.rollNo)

stud1 = School("Raja", "21CA020")

stud1.studDetails()

'''o/P:
Details :
Stud name: Raja
stud RollNo: 21CA020
'''

#         Structure is also within the Constructor
'''
class School:
    def __init__(self, name, rollNo):
        self.name = name  # variable can be same or different
        self.rollNo = rollNo
        print("Details :", "\nStud name:", self.name, "\nstud RollNo:", self.rollNo)

stud1 = School("Raja", "21CA020")
'''
'''o/p:
Details : 
Stud name: Raja 
stud RollNo: 21CA020
'''