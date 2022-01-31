#                   class & object
'''
class Mobile:
    def configOfMobile(self): # 'def' is Method
        print("8gb, 256gb, sd845")

mobile1 = Mobile() #'mobile1' is Object
mobile2 = Mobile()
print(type(com1))

Mobile.configOfMobile(com1) # Mostly it won't use
Mobile.configOfMobile(com2)
print()
mobile1.configOfMobile() # Mostly it use
mobile2.configOfMobile()
'''
'''o/p:
<class '__main__.Mobile'>
8gb, 256gb, sd845
8gb, 256gb, sd845

8gb, 256gb, sd845
8gb, 256gb, sd845
'''

#             To see in-built code
# ctrl + click on function()

# a = 37
# b = a.bit_length()
# print(bin(37))
# print("Length is Binary: ", b)
'''o/p:
0b100101
Length is Binary:  6
'''