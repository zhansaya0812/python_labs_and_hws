def update_counts(d, items):
    for item in items:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
counts = {'apple': 2, 'banana': 1}
new_items = ['apple', 'orange', 'apple']
print(update_counts(counts, new_items))
