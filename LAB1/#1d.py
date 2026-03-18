def invert_unique(d):
    inverted={}
    for key, value in d.items():
        if value not in inverted:
            inverted[value]=[]
        if key not in   inverted[value]:
            inverted[value].append(key)
    return inverted
data={"a":1,"b":2,"c":2,"d":1,"e":2}
print(invert_unique(data))
