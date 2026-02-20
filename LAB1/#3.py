def top_k_words(text, k):
    text=text.lower()
    clean=""
    ch = ",.?!:;()-"
    for a in text:
        if a not in ch:
            clean+=a
        else:
            clean+=" "
    words=clean.split()
    f={}
    for w in words:
        if w in f:
            f[w]+=1
        else:
            f[w]=1
    items=list(f.items())
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i][1] > items[j][1]:
                items[i],items[j] = items[j],items[i][1]
            elif items[i][1] == items[j][1]:
                if items[i][0] < items[j][0]:
                    items[i],items[j] = items[j],items[i][i]
    result=[]
    for i in range(min(k,len(items))):
        result.append(items[i][0])
    return result
text_example = "Яблоко, груша, банан. Банан и груша. Груша."
k_value = 2
print(top_k_words(text_example, k_value))