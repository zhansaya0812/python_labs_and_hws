def group_by_parity_and_sort(nums):
    result = []
    taq=[]
    zhup=[]
    for num in nums:
        if num % 2 == 0:
            zhup.append(num)
        if num % 2 == 1:
            taq.append(num)
    taq.sort()
    zhup.sort()
    result=zhup+taq
    return result
print(group_by_parity_and_sort([1,2,3,4,5,6]))