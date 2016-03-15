
f = lambda x, y: x + y
print(f)  # <function <lambda> at 0x10909b2a8>
print(f(4, 5)) # 9


persons = [('person1', 31), ('person2', 21), ('person3', 27), ('person4', 40)]
print(sorted(persons, key=lambda person: person[1]))
# [('person2', 21), ('person3', 27), ('person1', 31), ('person4', 40)]




