#                  Duck Typing

# If its looks like a duck,walk like a duck,quack like a duck
# and then it probably is a duck.

# ide Integrated Development Environment.
# ide is something user is defining a Method.
# if create ide we have to create own class.
# 'ide' is not fixed to one class it is Dynamic to more than one class.
'''
class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = pycharm()

lap1 = Laptop()

lap1.code(ide)
'''
'''o/p:
Compiling
Running
'''

# 'ide' is not fixed to one class it is Dynamic to more than one class
# if there is an object which is 'ide' and it has the method what we called that's it.
# we will not concern about which class object it is that ide
# we will concern only That class should have method of ide

class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
class Laptop:
    def code(self, ide):
        ide.execute()

ide1 = pycharm()
ide2 = MyEditor()

lap1 = Laptop()

lap1.code(ide1)
lap1.code(ide2)
'''o/p:
Compiling
Running
Spell check
Convention check
'''