def max_subarray_sum(nums,k):
    max_sum=None
    for i in range(len(nums)-k+1):
        subarray=nums[i:i+k]
        invalid=False
        count=0
        for num in subarray:
            if num<=0:
                invalid=True
                break
            count+=num
        if not invalid:
            if max_sum is None or count>max_sum:
                max_sum=count
    return max_sum
print(max_subarray_sum([1, 5, 2, 0, 8, 3, 1], 3)) 