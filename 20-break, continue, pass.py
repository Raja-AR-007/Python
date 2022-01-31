#                          break
# break is used to jump out of the loop based on condition.

# Candy Program
'''
available = 5
a = int(input("How many candies you want: "))
i = 1
while i <= a:
    if i > available:
        print("stock is only 5")
        break
    print("candy")
    i += 1
print("Bye")
'''
'''o/p:
How many candies you want: 10
candy
candy
candy
candy
candy
stock is only 5
Bye
'''

#                           continue
# continue is used to skip some condition.

#       skipping the no. which is divisible by both 3 and 5
'''
for i in range(10,21):
    if i%3==0 and i%5==0:
        continue
    print(i)
'''
'''o/p:
10
11
12
13
14
16
17
18
19
20
'''

#                         pass
# if one block only having pass keyword
# it will just pass the particular block even without having any statements

for i in range(1,11):
    if i%2 != 0:
        pass
    else:
        print(i)
'''o/p:
2
4
6
8
10
'''