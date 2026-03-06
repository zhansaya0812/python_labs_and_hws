#ITERATORS&COMPREHENSION
#1
square=[i for i in range(1,21) if i%2==0]
print(square)
#2
matrix = [[1,2,3], [4,5,6], [7,8,9]]
new_list=[(lambda x:x[0]*x[1]*x[2])(row) for row in matrix]
print(new_list)
#3
words = ["кот", "машина", "ананас", "дом","лимон "]
new_list=[w for w in words if len(w)>4 and "а" not in w]
print(new_list)
#[] is result without lemon
#4
numbers = [1,2,3,4,5]
new_list={x: ("чётное" if x%2==0 else "нечётное") for x in numbers}
print(new_list)
#5
matrix = [[1,2], [3,4], [5,6]]
new_list=[x for row in matrix for x in row]
print(new_list)
#6
numbers =list(range(1,21))
check=[
    "Fizzbuzz" if x%15==0 else
    "Buzz" if x%5==0 else
    "Fizz"if x%3==0 else
     x
    for x in numbers
]
print(check)
#