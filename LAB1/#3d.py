def merge_dicts_sum(dict1, dict2):
    result = dict1.copy()
    for key,value in d2.items():
        if key in result:
            result[key]+=value
        else:
            result[key]=value
    return result
d1={"apple":15,"orange":25,"banana":30}
d2={"apple":10,"orange":35,"banana":5}
print(merge_dicts_sum(d1,d2))
