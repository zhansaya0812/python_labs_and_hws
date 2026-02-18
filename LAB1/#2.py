#2
process= lambda s: " ".join(
    filter(
        lambda w:len(w)%2==0,
        map(
            lambda w:w[::-1],
            filter(lambda w: all(ch<'0'or ch>'9'for ch in w),s.split())
        )
    )
)
print(process(" hello lambda world1"))