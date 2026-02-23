process=lambda s: list(
    filter(
        lambda w:w[0].lower()==w[-1].lower(),
        filter(
            lambda w: w.lower()!=w[::-1].lower(),
            filter(
                lambda w: len(w)>3,
                s.split()
            )
        )
    )
)
print(process("hello aurora"))