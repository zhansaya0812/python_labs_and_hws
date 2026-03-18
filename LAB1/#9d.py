def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result=set()
    for item in sets_list[0]:
        result.add(item)
    for i in range(1,len(sets_list)):
        current=sets_list[i]
        common=set()
        for element in result:
            if element in current:
                common.add(element)
        result=common
        if not result:
            break
    return result
data = [
    {1, 2, 3, 4},
    {2, 3, 5, 8},
    {0, 2, 3, 10}
]
print(common_elements_all(data))
