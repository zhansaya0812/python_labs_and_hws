def deep_sum(d):
    total = 0
    for key in d:
        value = d[key]
        if type(value) == int or type(value) == float:
            total+=value
        elif type(value) == list:
            for item in value:
                total+=item
        elif type(value) == dict:
            total+=deep_sum(value)
    return total
data = {
    "a": 10,
    "b": [1, 2, 3],
    "c": {"d": 5, "e": [10, 20]},
    "f": 4
}
print(deep_sum(data))
