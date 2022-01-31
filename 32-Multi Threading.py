#                 Multi Threading

# Multi Threading means we execute Multiple threads simultaneously.

# Normally we work on Main Thread

# Now we creating two Threads in Main Thread.
# Before creating Thread we need to import all threading features.
# classes should be Subclass of Thread then only we can perform Multi threading.
# In classes we need name all methods as run() method and call it as start() method.
'''
from threading import *

class Hello(Thread):  # Thread1
    def run(self):
        for i in range(500):
            print("Hello")

class Hi(Thread):  # Thread2
    def run(self):
        for i in range(500):
            print("Hi")

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()
'''
'''o/p:
both calsses's methods will run parallely
'''

#            Time scheduler for Multi threading

# importing sleep() method from time.
'''
from time import sleep
from threading import *

class Hello(Thread):  # Thread1
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):  # Thread2
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()
'''
'''
o/p: two threads going to the CPU at same time so it Giving Collision output
Hello
Hi
Hi
Hello
Hello
Hi
HiHello

Hello
Hi
'''

#                join() method

# Now it Giving Proper Parallel Output
'''
Main Thread
t1 Thread
t2 Thread
'''

from time import sleep
from threading import *

class Hello(Thread):  # Thread1
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):  # Thread2
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()  # t1 Thread
sleep(0.2)
t2.start()  # t2 Thread

t1.join()
t2.join()
print("Bye")  # Main Thread

'''o/p:
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
'''