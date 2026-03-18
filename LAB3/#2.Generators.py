#GENERATORS(4)
#1
def even_numbers(n):
    for x in range(1,n+1):
         if x%4==0:
             yield "кратно 4"
         else:
             yield x
for x in even_numbers(10):
    print(x)
#2
def filter_words(words):
    for word in words:
        if "а" in word.lower():
            yield "c a"
        elif len(word)>4:
            yield word
    #filtered=lambda wo: "c a" if "а" in wo.lower() else wo
    #return(filtered(word) for word in words if len(word)>4)
words=["кот", "машина", "дом", "арбуз"]
for w in filter_words(words):
    print(w)
#3
def infinite_numbers():
    #check=lambda x: "FizzBuzz" if x%15==0 else("Fizz" if x%3==0 else("Buzz" if x%5==0 else x))
    #num=1
    #while True:
    #yield check(num)
    #num+=1
    x=1
    while True:
        if x%15==0:
            yield "FizzBuzz"
        elif x%3==0:
            yield "Fizz"
        elif x%5==0:
            yield "Buzz"
        else:
            yield x
        x+=1
#for x in infinite_numbers():
    #print(x) infinitive doesnt stop
g=infinite_numbers()
for x in g:
    print(x)
    if x=="FizzBuzz":
        break #stops when we get FizzBuzz
#or print(next(g))
#4
def squares(n):
    for x in range(1,n+1):
        if (x**2)%2==0:
            yield "чётный квадрат"
        else:
            yield x**2
for x in squares(5):
    print(x)
#