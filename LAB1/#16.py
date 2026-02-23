def transform_list(nums):
    result = []
    for num in nums:
        if num<0:
            continue
        if num%2==0:
            result.append(num**2)
        elif num%2!=0 and num>10:
            digits=0
            for digit in str(num):
                digits+=int(digit)
            result.append(digits)
        else:
            result.append(num)
    return result
print(transform_list([1,-2,46,11,5]))
