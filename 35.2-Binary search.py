#          Binary Search

pos = -1  # global variable
def binarySearch(list, n):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid = (lower + upper) // 2   # mid is 'i'
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower = mid+1
            else:
                upper = mid-1
    return False
list = [12, 34, 45, 49, 56, 78, 81]
n = 81
if binarySearch(list, n):
    print("Found at position %d" %(pos),'direct len(position) is',  pos+1)  # 'pos' will give position of value
else:
    print("Not found")
'''o/p:
Found at position 6 direct len(position) is 7
'''