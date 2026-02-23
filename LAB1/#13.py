def replace_every_nth(text, n, char):
    numbers="0123456789"
    result=[]
    count=0
    words=text.split(' ')
    for i,word in enumerate(words):
        processed_word=""
        for w in word:
            if w not in numbers and len(word)>=3:
               count+=1
               if count%n==0:
                   processed_word+=char
               else:
                   processed_word+=w
            else:
                processed_word+=w
    result.append(processed_word)
    return " ".join(result)
print(replace_every_nth("hello aurora",3,"*"))