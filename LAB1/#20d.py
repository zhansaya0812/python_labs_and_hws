process=lambda d: sorted(d.keys(), key=lambda k:(d[k],len(k)))[::3]
data={
    "a":10,
    "b":20,
    "c":10,
    "d":5,
    "e":10
}
print(process(data))