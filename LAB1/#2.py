#2
process= lambda s: " ".join(
    map(
        lambda w:w[::-1],
        filter(
            lambda w: all(ch<'0'or ch>'9'for ch in w) and len(w)%2==0,
               s.split()
        )
    )
)