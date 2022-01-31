#                         user input() function

#In python by default user input data type is String

x = input("Enter x value: ")
print(type(x)) #<class 'str'>
a = int(x)
y = input("Enter Y value: ")
b = int(y)
c = a + b
print(c)
'''o/p:
Enter x value: 4
<class 'str'>
Enter Y value: 3
7
'''

# or

# x = int(input("Enter x value: "))
# y = int(input("Enter y value: "))
# z = x + y
# print(z)
'''o/p:
Enter x value: 5
Enter y value: 4
9
'''

#                      character input()

# char = input("Enter a char: ")
# print(char[0])

# or

# char = input("Enter a char: ")[0]
# print(char)
'''o/p:
Enter a char: vjei
v
'''

#                         evaluate input function 'eval()'

# math = eval(input("Enter a expression: "))
# print(math)
'''o/p:
Enter a expression: 2 + 4 - 5 * 3 / 3
1.0
'''

#                         Command Promt user input using folder
# Save this code in Desktop
# Run this code as folder in cmd promt

# import sys

# x = int(sys.argv[1]) #'argv' means argument values
# y = int(sys.argv[2])
# z = x + y
# print(z)