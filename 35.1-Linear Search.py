#                linear search

# It will search values one by one
pos = -1
def linearSearch(list, n):
    i = 0
    while i <= len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i =i + 1
        return False

list = [1,4,3,5,6]
n = 1
if linearSearch(list, n):
    print("Found at", pos, "direct position is", pos+1)
else:
    print("Not found")

# o/p: Found at position 0 direct position is 1

'''
list = [2, 32,  5, 4]
n = 3
if n in list:
    print("found")
print("Not found")
'''
# o/p: found

