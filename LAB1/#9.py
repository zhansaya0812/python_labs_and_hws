def alternate_case_blocks(text,n):
    text=text.replace(" ", "")
    blocks = []
    for i in range(0,len(text),n):
        c=text[i:i+n]
        index=i//n
        if index%2==0:
            blocks.append(c.upper())
        else:
            blocks.append(c.lower())
    return "".join(blocks)
print(alternate_case_blocks("apple 2latte juice", 3))