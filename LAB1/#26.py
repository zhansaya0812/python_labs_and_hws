def remove_duplicates_keep_last(nums):
    result=[]
    seen = set()
    for i in range(len(nums)-1,-1,-1):
        num=nums[i]
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result[::-1]
print(remove_duplicates_keep_last([1,2,3,2,1]))