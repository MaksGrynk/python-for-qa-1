

test_list = [1, 2, 'a', 'b', '3', 4, 5]
ints = filter(lambda x: isinstance(x, int), test_list)
print(ints)

multiple = map(lambda x: x * 2, ints)
print(multiple)

result = reduce(lambda x, y: x + y, multiple)
print(result)
