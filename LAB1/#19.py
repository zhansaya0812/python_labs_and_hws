process=lambda l1,l2: list(
    map(
        lambda l:l[0],
        filter(
            lambda x:x[0]==x[1] and x[0]%2==0,
            zip(l1,l2)
        )
    )
)
l1=[2,5,10,8,3,12]
l2=[2,5,11,8,3,13]
print(process(l1,l2))