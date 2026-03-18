def filter_by_digit_sum(nums):
    result=set()
    for num in nums:
        if num%2!=0:
            sum=0
            temp=num if num>=0 else -num
            while temp>0:
                sum+=temp%10
                temp//=10
            if sum%2==0:
                result.add(num)
    return result
data = {13, 22, 15, 31, 45, 11}
print(filter_by_digit_sum(data))


