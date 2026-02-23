process=lambda l1,l2:[
    x for x in l1
    if x not in l2 and x>(sum(l1)/len(l1))
]
l1=[10,40,10,50]
l2=[40,100]
print(process(l1,l2))