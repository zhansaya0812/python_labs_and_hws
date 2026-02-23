def common_unique_chars(s1,s2):
    numbers="0123456789"
    result=""
    for char in s1:
        if char in s2:
            if char!=" " and char not in numbers:
                if char not in result:
                    result+=char
    return result
s1="apple pie 123"
s2="orange juice 456"
print(common_unique_chars(s1,s2))