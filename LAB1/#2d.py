filtered=lambda s: set(filter(lambda x:x>(sum(s)/len(s)) and x%2!=0 and x%5!=0,s)) if s else set()
s={1, 3, 7, 10, 15, 21}
print(filtered(s))
