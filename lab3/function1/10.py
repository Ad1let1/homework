def uniques(nums):
    a = []
    for el in nums:
        if el not in a:
            a.append(el)
    return a


a = [1, 2, 2, 3, 4, 4, 5]
print(uniques(a)) 