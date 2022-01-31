#          Selection Sort

def selectionSort(nums):
    # takes min position 0 and 5 times  comparing
    for i in range(5):
        minposition = i
        # 6 is list length
        for j in range(i, 6):
            if nums[j] < nums[minposition]:
                minposition = j
        temp = nums[i]
        nums[i] = nums[minposition]
        nums[minposition] = temp
        print(nums)

nums = [41,22,72,84,62,31]
selectionSort(nums)
print("selection sort:",nums)
'''o/p:
[22, 41, 72, 84, 62, 31]
[22, 31, 72, 84, 62, 41]
[22, 31, 41, 84, 62, 72]
[22, 31, 41, 62, 84, 72]
[22, 31, 41, 62, 72, 84]
selection sort: [22, 31, 41, 62, 72, 84]
'''