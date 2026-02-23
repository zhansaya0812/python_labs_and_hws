def analyze_strings_list(words):
    words_list = []
    numbers="0123456789"
    for word in words:
        digit=False
        for char in word:
            if char in numbers:
                digit=True
                break
        if digit:
            continue
        if len(word)%2==0:
            new_word=word[::-1]
        else:
            new_word=word.upper()
        if new_word not in words_list:
            words_list.append(new_word)
    return words_list
print(analyze_strings_list(["cat","door","hello","cat","cat3"]))