top_5=lambda d:sorted(d.keys(),key=lambda k:(-d[k],k))[:5]
data={"apple":15,"orange":25,"banana":30}
print(top_5(data))