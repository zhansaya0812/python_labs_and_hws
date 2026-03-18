processed=lambda d:{
    key:sorted([x for x in value if x%2!=0])
    for key,value in d.items()
    if [x for x in value if x%2!=0]
}
data = {
    "a": [10, 2, 8],
    "b": [5, 1, 9, 3],
    "c": [14, 7, 2, 1],
    "d": []
}
print(processed(data))