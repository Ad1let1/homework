def has_33(nums):
    nums.append(0)
    for i in range(len(nums)):
        if(nums[i] == 3 and nums[i+1] == 3):
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))