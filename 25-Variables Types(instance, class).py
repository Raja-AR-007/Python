#                   Types of Variables

# Instance variable.
# Class variable or static variable.

# 'Instance variable' used in Constructor "__init__()".
# 'Class variable' used in class block. It is also called as 'Static variable'.
'''
class Car:
    wheels = 4  # Class or static variable (this value is same to all Objects)
    def __init__(self):
        self.mileage = 10  #Instance variable
        self.model = "BMW"

car1 = Car()
car2 = Car()

Car.wheels = 5 #changing class variable

car1.mileage = 8 #changing Instance variable

print(car1.mileage, car1.model, car1.wheels)
print(car2.mileage, car2.model, car2.wheels)
'''
'''o/p:
8 BMW 4
10 BMW 4
'''

#     structure() Method createn for clear o/p
'''
class Car:
    wheels = 4  # Class or static variable (this value is same to all Objects)
    def __init__(self):
        self.mileage = 10  #Instance variable
        self.model = "BMW"

    def structure(self):
        print("Mileage is :",self.mileage,',', "Model is :",self.model,',', "Wheels :",self.wheels)

car1 = Car()
car2 = Car()

Car.wheels = 5 #changing class variable

car1.mileage = 8 #changing Instance variable

car1.structure()
car2.structure()
'''
'''o/p:
Mileage is : 8 , Model is : BMW , Wheels : 5
Mileage is : 10 , Model is : BMW , Wheels : 5
'''