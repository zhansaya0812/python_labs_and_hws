#LABORATORY1
#LISTSANDSTRING
#1
def analyze_text(text):
    vowels = "aeiouy"
    uniq_v = ""
    words = []
    used = []
    cur = ""

    for ch in text.lower() + " ":
        if 'a' <= ch <= 'z':
            cur += ch

            for v in vowels:
                if ch == v and ch not in uniq_v:
                    uniq_v += ch
        else:
            if cur != "":
                l = 0
                for _ in cur:
                    l += 1

                if l >= 5 and cur[0] == cur[l-1] and cur not in used:
                    words += [cur]
                    used += [cur]
                cur = ""
    c = 0
    for _ in uniq_v:
        c += 1
    res = ""
    for i in range(len(words)):
        if i > 0:
            res += " "
        res += words[i]

    return (c, res)
print(analyze_text("ROTATOR"))