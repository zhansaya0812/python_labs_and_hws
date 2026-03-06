#LAMBDAFUNCTIONS(6)
#1
check=lambda x:"положительное" if x>0 else ("отрицательное" if x<0 else "ноль")
print(check(5))
print(check(-3))
print(check(0))
#2
words= ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words=sorted(words, key=lambda word:len(word))
print(sorted_words)
#3
numbers = [5, 12, 7, 20, 33, 8]
process=list(filter(lambda x:x>10 and x%2==0, numbers))
print(process)
#4
numbers = [1, 2, 3, 4, 5, 6]
process=list(map(lambda x:x**2 if x%2==0 else (x*3),numbers))
print(process)
#5
compare=lambda a,b:"a больше" if a>b else("b больше" if b>a else "равны")
print(compare(10,7))
print(compare(3,5))
print(compare(4,4))
#6
numbers = [0, -3, 5, -7, 8]
new_list=[(lambda x:"положительное" if x>0 else ("отрицательное" if x<0 else "ноль"))(n) for n in numbers]
print(new_list)
