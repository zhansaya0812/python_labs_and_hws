def filter_sets(sets_list):
    filtered=[]
    for s in sets_list:
        if len(s)<=3:
            continue
        negative=False
        even=False
        for num in s:
            if num<0:
                negative=True
            if num%2==0:
                even=True
        if not negative and even:
            filtered.append(s)
    return filtered
data=[
    {2,4,6,8},
    {1,3,7,9},
    {10,20,-2,25},
    {2,5},
    {1,3,7,10}
]
print(filter_sets(data))