process=lambda strings:sorted(
    strings,
    key=lambda x: (-len(x), x.lower())
)[:5]
print(process( ["apple", "banana", "kiwi", "cherry", "pear", "fig", "apricot"]))