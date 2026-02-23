def flatten_and_filter(first):
    result = []
    for item in first:
        if type(item)==list:
            result.extend(flatten_and_filter(item))
        elif type(item) in [int, float]:
           if item>0 and item%4!=0 and item>9:
               result.append(item)
    return sorted(result)
print(flatten_and_filter( [12, [5, 22, [100, 4, 13]], 8, [44, 17], 3]))
