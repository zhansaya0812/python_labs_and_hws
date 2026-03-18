def top_k_frequent(nums, k):
    count={}
    for num in nums:
        if num not in count:
            count[num]=0
        count[num]+=1
    items=[]
    for num in count:
        items.append([num,count[num]])
    n_items=len(items)
    for i in range(n_items):
        for j in range(0,n_items-i-1):
            num_a,freq_a=items[j]
            num_b,freq_b=items[j+1]
            if freq_a<freq_b or (freq_a==freq_b and num_a>num_b):
                items[j],items[j+1]=items[j+1],items[j]
    result=set()
    limit=k if k<len(items) else len(items)
    for i in range(limit):
        result.add(items[i][0])
    return result
data=[1,1,1,2,2,3,4,4]
k=2
print(top_k_frequent(data,k))