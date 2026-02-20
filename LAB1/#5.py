def compress_text(text):
    if not text:
        return ""
    result = ""
    i=0
    n = len(text)
    while i<n:
        char = text[i]
        count=0
        while i+count<n and text[i+count].lower()==char.lower():
            count+=1
        if count>1:
            result+= char+str(count)
        else:
            result+= char
        i+=count
    return result
print(compress_text("aaBBcDDD"))