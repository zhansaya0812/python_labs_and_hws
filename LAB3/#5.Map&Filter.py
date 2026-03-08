#MAP&FILTER
#1
numbers=[1,2,3,4,5]
process=list(map(lambda x:x*2,numbers))
print(process)
#2
words = ["кот", "машина", "арбуз", "дом"]
processed = list(map(lambda w:w.upper()+ "!" if len(w)>3 else w.upper(),words))
print(processed)
#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens=list(filter(lambda x:x%2==0, numbers))
print(evens)
#4
numbers = [0, 5, 12, 7, 20, -3, 8]
processed = list(map(lambda x:x/2 if x%2==0 else x*3,
filter(lambda x:x>5, numbers)))
print(processed)