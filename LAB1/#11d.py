def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        duplicate = False
        for w in result[length]:
            if w==word:
                duplicate = True
                break
        if not duplicate:
            result[length].append(word)
    return result
data=["apple","banana","cat","dog","banana"]
print(group_by_length(data))