def count_vowels(word):
    l="аеёиоуыэюяaeiouy"
    count=0
    for char in word.lower():
        if char in l:
            count+=1
    return count
def sort_(text):
    words=text.split()
    groups={}
    for word in words:
        length=len(word)
        if length not in groups:
            groups[length]=[]
        groups[length].append(word)
    sorted_lengths=sorted(groups.keys())
    result=[]
    for length in sorted_lengths:
        current=groups[length]
        l=[]
        for w in current:
            l.append((-count_vowels(w),w.lower(),w))
        l.sort()
        for item in l:
            result.append(item[2])
    return result
print(sort_("pear avocado apple  "))
