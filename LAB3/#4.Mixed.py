#MIXED
#1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def special_numbers(n):
    for i in range(1,n+1):
        if i%15==0:
            yield "FizzBuzz"
        elif i%3==0:
            yield "Fizz"
        elif i%5==0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for x in special_numbers(10):
    print(x)
#2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
new_list=[(lambda w: (w.upper() if len(w)>4 else "short")+("*" if "a" in w.lower() else ""))(w) for w in words]
print(new_list)
#3
def process_numbers(numbers):
    filtered=filter(lambda x:x>=0, numbers)
    check=map(
        lambda x:x/2 if x%2==0 else x*3+1,filtered
    )
    yield from check
numbers=[5,-2,8,0,-7,3]
for x in process_numbers(numbers):
    print(x)
#4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
check=lambda s:("Отлично" if s>=90 else("Хорошо" if s>=70 else "Удовлетвортельно"))
dict={name: check(score)for name,score in students}
print(dict)
#5
def matrix_transform(matrix):
     for row in matrix:
         for num in row:
            if num % 2 == 0 and num % 3 == 0:
                yield "кратно 6"
            elif num%2==0:
                yield "чётное"
            elif num%3==0:
                yield "кратно 3"

            else:
                yield num

matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)


