def invert_dict_strict(d):
    count={}
    for value in d.values():
        if value not in count:
            count[value]=0
        count[value]+=1
    result={}
    for key,value in d.items():
        if count[value]==1:
            result[value]=key
    return result
data={
    "a":1,
    "b":2,
    "c":1,
    "d":3,
    "e":4,
    "f":2
}
print(invert_dict_strict(data))