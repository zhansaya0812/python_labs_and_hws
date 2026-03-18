def sort_dict_by_value_sum(d):
    items=[]
    for key in d:
        current_sum=0
        for num in d[key]:
            current_sum+=num
        items.append([key, current_sum])
    n=len(items)
    for i in range(n):
        for j in range(0,n-i-1):
            key_a,sum_a=items[j]
            key_b,sum_b=items[j+1]
            if sum_a<sum_b or (sum_a==sum_b and key_a>key_b):
                items[j],items[j+1]=items[j+1],items[j]
    result=[]
    for item in items:
        result.append((item[0],item[1]))
    return result
data={
    "a":[1,2,3],
    "b":[4,5,6],
    "c":[7,8,9]
}
print(sort_dict_by_value_sum(data))