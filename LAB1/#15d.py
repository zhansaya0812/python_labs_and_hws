process=lambda d:{
    k:v for k,v in d.items()
    if v>=(sum(d.values())/len(d)) and v%2!=0
} if d else {}
data={
    "a":1,
    "b":2,
    "c":1,
    "d":3,
    "e":4,
    "f":5
}
print(process(data))