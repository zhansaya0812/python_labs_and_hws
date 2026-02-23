process_text = lambda text: " ".join([
    word if any(char in "0123456789" for char in word) else
    "VOWEL" if word[0].lower() in 'aeiouyаеёиоуыэюя' else
    "CONSONANT"
    for word in text.split()
])
print(process_text("apple 2latte juice"))