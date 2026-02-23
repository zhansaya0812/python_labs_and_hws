def longest_increasing_sublist(nums):
    if not nums:
        return []
    max_sub=[]
    current=[nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            current.append(nums[i])
        else:
            if len(current)>len(max_sub):
                max_sub=current
            current=[nums[i]]
    if len(max_sub)>=len(current):
        return max_sub
    else:
        return current
print(longest_increasing_sublist([1, 2, 3, 0, 4, 5, 6, 7, 1]))