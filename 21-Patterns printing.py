#                        Print patterns

#                  square pattern
'''
for j in range(4):
    print("# ", end="")
print()
for j in range(4):
    print("# ", end="")
print()
for j in range(4):
    print("# ", end="")
print()
for j in range(4):
    print("# ", end="")
'''
'''o/p:
# # # #
# # # #
# # # #
# # # #
'''

# or
'''
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
'''
'''o/p:
# # # #
# # # #
# # # #
# # # #
'''
#                    half square pattern
# for i in range(4):
#     for j in range(i+1): # 'i+1' avoiding 0th position
#         print("# ", end="")
#     print()

# or

# for i in range(1, 5):
#     for j in range(i):
#         print("# ", end="")
#     print()

'''o/p:
# 
# # 
# # # 
# # # # 
'''
#                  Downwards

# for i in range(4):
#     for j in range(4-i):
#         print("# ", end="")
#     print()

# or

# for i in range(1,5):
#     for j in range(4-i+1):
#         print("# ", end="")
#     print()
'''o/p:
# # # # 
# # # 
# # 
# 

'''
#           range(0) won't print anything
for i in range(0):
    print("raja")
'''o/p:
empty
'''