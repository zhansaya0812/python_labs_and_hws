l="аеёиоуыэюяaeiouy"
n="0123456789"
process=lambda s: ",".join(
    filter(
        lambda w:len(set(c.lower() for c in w if c not in n))>3
        and not any(w.lower().count(v)>1 for v in l),
        s.split(),
    )
)
print(process('hello w2 qazaq'))
