process=lambda s: " ".join(
    filter(
        lambda w:len(w)>4,
        filter(
            lambda w:len(w.lower())==len(set(w.lower())),
            filter(
                lambda w: all(ch<'0'or ch>'9'for ch in w),s.split()
            )
        )
    )
)
print(process("python abcd123"))