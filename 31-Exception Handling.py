#               Exception Handling

# It is used to giving reason for run time error, so that
# the program can continue the process

# In the next program we creating Message for this error that is
# ZeroDivisionError
'''
a = 1
b = 0
print(a/b)
'''
'''o/p:
ZeroDivisionError: division by zero
'''

'''
a = 1
b = 0
try:
    print(a/b)
    
except Exception as e:      # or name as ZeroDivisionError
    print("Hey, You can't divide a number by Zero")
    print('Actual Error is:', e)
'''
'''o/p:
Hey, You can't divide a number by Zero
Actual Error is: division by zero
'''

# closing the exception after the process
'''
a = 1
b = 0
try:
    print("resource opened")
    print(a/b)
    print("resource closed")
    
except Exception as e:
    print("Hey, You can't divide a number by Zero")
    print('Actual Error is:', e)
    print("resource closed")
'''
'''o/p:
resource opened
Hey, You can't divide a number by Zero
Actual Error is: division by zero
resource closed
'''

#        finally block

# finally block will execute either the runtime error found or not
'''
a = 1
b = 1
try:
    print("resource opened")
    print(a/b)
    
except ZeroDivisionError as e:
    print("Hey, You can't divide a number by Zero")
    print('Actual Error is:', e)   
    
finally:
    print("resource closed")
'''
''''o/p:
resource opened
1.0
resource closed
'''

# Adding value error also in try block
'''
k = int(input("Enter a number:"))
print(k)
'''
'''o/p:
Enter a number:g
ValueError: invalid literal for int() with base 10: 'g'
'''


# Exception for two errors
'''
a = 1
b = 1  # watch the value
try:
    print("resource opened")
    print(a/b)                # ZeroDivisionError
    k = int(input("Enter a number:"))
    print(k)                  # ValueError
 
except ZeroDivisionError as e:
    print("Hey, You can't divide a number by Zero")
    print('Actual Error is:', e)

except Exception as v:  # or ValueError
    print("Invalid value")
    print('Actual Error is:', v)

finally:
    print("resource closed")
'''
'''o/p:
resource opened
1.0
Enter a number:p
Invalid value
Actual Error is: invalid literal for int() with base 10: 'p'
resource closed
'''

# Adding this list error
'''
list = [2,3,4]
print(list[3])
'''
'''o/p:
IndexError: list index out of range
'''

# Exception will handle all the errors 'next program for example'

# If there is RunTime error then only Exceptions will work

a = 1
b = 1  # watch the value
try:
    print("resource opened")
    print(a/b)             # ZeroDivisionError
    k = int(input("Enter a number:"))
    print(k)               # ValueError
    list = [2,3,4]
    print(list[3])         # Exception

except ZeroDivisionError as e:
    print("Hey, You can't divide a number by Zero")
    print('Actual Error is:', e)

except ValueError as v:
    print("Invalid value")
    print('Actual Error is:', v)

except Exception as e:  # or IndexError
    print("Something went wrong..., ")
    print('Actual Error is:', e)

finally:
    print("resource closed")

'''o/p:
resource opened
1.0
Enter a number:6
6
Something went wrong..., 
Actual Error is: list index out of range
resource closed
'''


# Exception will handle all the errors
'''
a = 1
b = 1  # watch the value
try:
    print("resource opened")
    print(a/b)             # ZeroDivisionError
    k = int(input("Enter a number:"))
    print(k)               # ValueError
    list = [2,3,4]
    print(list[3])         # Exception

except Exception as e:  # Alias 'e' will give the actual Error
    print("Something went wrong..., ",'Actual Error is:', e)

finally:
    print("resource closed")
'''
'''o/p:
resource opened
1.0
Enter a number:6
6
Something went wrong..., 
Actual Error is: list index out of range
resource closed
'''