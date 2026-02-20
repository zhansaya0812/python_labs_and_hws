def palindrome_words(text):
    clean = ""
    ch ="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for a in text:
        if a not in ch:
            clean += a
        else:
            clean += " "
    words = clean.split()
    f=[]
    for w in words:
        if w.lower() == w.lower()[::-1] and len(w)>=3:
            f.append(w)
    f.sort(key=lambda x: (-len(x), x.lower()))
    return f
print(palindrome_words("Anna is qazaq girl?"))





