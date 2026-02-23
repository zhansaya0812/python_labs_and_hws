def moving_average(nums, k):
    averages=[]
    for i in range(len(nums)-k+1):
        window=nums[i:i+k]
        negative=False
        for  n in window:
            if n<0:
                negative=True
                break
        if not negative:
            averages.append(sum(window)/k)
    return averages
print(moving_average([1,2,3,-1,4,5],2))