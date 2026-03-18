set_lambda=lambda set1,set2:{x for x in (set1|set2)-(set1&set2) if x%2==0}
set1={1,2,3,4,5}
set2={1,2,7,8,5}
print(set_lambda(set1,set2))