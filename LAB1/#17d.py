get_triple_set = lambda s1, s2, s3: (s1 & s2) - s3
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {4, 5, 7}
print(get_triple_set(set_a, set_b, set_c))
