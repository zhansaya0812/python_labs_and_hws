process=lambda lists:[
    sum(l1)/len(l1)
    for l1 in lists
    if len(l1)>=3 and sum(l1)%2==0
]
print(process([[1, 2, 3], [10, 20], [4, 4, 4, 4]]))