#                               List[]

# List value is Mutable or changable 
# List will give sequence or same value.

num = [12, 34, 23, 56, 67]
print(num[0]) #12

print(num[4]) #67

print(num[2:]) #[23, 56, 67]

print(num[:3]) #[12, 34, 23]

print(num[2:4]) #[23, 56]

print(num[-4:]) #[34, 23, 56, 67]

# ['taking from given -ve value' : 'deleting from given -ve value'] only for negative values

print(num[:-3]) #[12, 34]   

print(num[-3:]) #[23, 56, 67]

print(num[-5:-1]) #[12, 34, 23, 56]


#                         functions of List


#                     append()

num = [12, 34, 23, 56, 67]
num.append(80)
print(num)
# o/p: [12, 34, 23, 56, 67, 80]

#                     pop()

num1 = [12, 34, 23, 56, 67]
num1.pop() # stack deletion concept
print(num1)
# o/p: [12, 34, 23, 56]

num5 = [12, 34, 23, 56, 67]
num5.pop(2) # index value (we can delete mentioned position)
print(num5)
# o/p: [12, 34, 56, 67]

#                     insert()

num3 = [12, 34, 23, 56, 67]
num3.insert(1, 66) #we can insert a value in particular position
print(num3)
# o/p: [12, 66, 34, 23, 56, 67]

#                       remove()
num4 = [12, 34, 23, 56, 67]
num4.remove(34) #we can remove mentioned value
print(num4)
# o/p: [12, 23, 56, 67]

#                        del

num6 = [12, 34, 23, 56, 67]
del num6[0]
print(num6)
# o/p: [34, 23, 56, 67]

num7 = [12, 34, 23, 56, 67]
del num7[-5:-1]
print(num7)
# o/p: [67]

#                       extend()

num8 = [12, 34, 23, 56, 67]
num8.extend(["taj", 66, "raj"]) #we can give multiple different values
print(num8)
# o/p: [12, 34, 23, 56, 67, 'taj', 66, 'raj']


#                         min()

num9 = [12, 34, 23, 56, 67]
print(min(num9))
# o/p: 12

#                          max()
num10 = [12, 34, 23, 56, 67]
print(max(num10))
# o/p: 67

#                           sort()
num11 = [12, 34, 23, 56, 67]
num11.sort()  # assending order
print(num11)
# o/p: [12, 23, 34, 56, 67]

#                           count()

num12 = [12, 12, 23, 12, 67]
countNum = num12.count(12)  
print(countNum)
# o/p: 3
