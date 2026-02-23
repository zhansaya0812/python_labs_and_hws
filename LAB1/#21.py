process=lambda l: list(
    map(
        str.upper,
        filter(
            lambda s: s.isalpha()
            and len(s)>4
            and len(set(s.lower()))==len(s),
            l
        )
    )
)
test_data = ["Python", "Apple", "12345", "Box", "Экран", "Music"]
print(process(test_data))