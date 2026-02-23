p=lambda n:n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
process=lambda nums:[
    val for idx,val in enumerate(nums)
    if p(idx) and val%2!=0 and val>(sum(nums)/len(nums))
]
print(process([10,10,45,55,10,99]))