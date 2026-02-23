process=lambda nums: list(
    map(
        lambda x:x**2,
        filter(
            lambda x:(x%3==0 or x%5==0)
            and x%15!=0
            and len(str(abs(x)))%2 != 0,
            nums
        )
    )
)

print(process([9,15,45,100,25,75]))
