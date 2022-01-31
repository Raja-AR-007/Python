#               Bubble sort

def bubbleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [4,2,7,8,6,3]
bubbleSort(nums)
print(nums)

# o/p: [2, 3, 4, 6, 7, 8]