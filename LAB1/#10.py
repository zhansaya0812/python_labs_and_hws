num="0123456789"
count=0
process=lambda s: len(list(
    filter(
        lambda w: len(w) >= 5,
        filter(
            lambda w: w[0] not in num,
            filter(
                lambda w: any(ch in num for ch in w), s.split(),
                )
            )
        )
    )
)
print(process('hello w2orld'))