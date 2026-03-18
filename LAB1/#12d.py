filtered=lambda s:{
    word for word in s
    if len(word)>4
    and len(set(word))==len(word)
    and all('a'<=char.lower()<='z'or 'а'<=char.lower()<='я'for char in word)
}
data={"apple","banana","cat","dog","0812","hello!","stray"}
print(filtered(data))