def sort_dict_by_value_length(d):
    items=[]
    for key in d:
        items.append((key,d[key]))
    n=len(items)
    for i in range(n):
        for j in range(0,n-i-1):
            key_a,val_a=items[j]
            key_b,val_b=items[j+1]
            if len(val_a)>len(val_b) or len(val_a)==len(val_b) and key_a>key_b:
                items[j],items[j+1]=items[j+1],items[j]
    return items
data = {
    "cat": "meow",
    "dog": "woof",
    "bird": "tweet",
    "ant": "tiny"
}
print(sort_dict_by_value_length(data))