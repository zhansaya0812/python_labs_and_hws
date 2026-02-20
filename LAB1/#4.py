letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
process=lambda s: " ".join(
    map(
        lambda w:w.lower(),
        filter(
            lambda w:(
                sum(1 for c in w if c in letters)==1
                and w[0] not in letters
                and w[-1] not in letters
            ),
            s.split()
        )
    )
)
print(process("hEllo pYthon World"))


